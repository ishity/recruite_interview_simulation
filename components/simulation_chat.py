from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage
from dotenv import load_dotenv
import os
import streamlit as st

def simulation(situation):
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    
    llm = ChatOpenAI(temperature=0, openai_api_key=api_key)

    # セッション状態の初期化
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'first_input' not in st.session_state:
        st.session_state.first_input = ""
    if 'isScoring' not in st.session_state:
        st.session_state.isScoring = False

    # チャット履歴を取得
    messages = st.session_state.get('messages', [])

    input_hint = ""
    if "就活生" in situation:
        input_hint = "就活生に質問しよう！"
    else:
        input_hint = "面接官の質問に答えよう！"

    if st.session_state.isScoring == False:
        if st.session_state.first_input != "":
            # 最初のメッセージを送信
            if st.session_state.messages == []:
                st.session_state.messages.append(HumanMessage(content=st.session_state.first_input))
                with st.spinner("Loading..."):
                    response = llm(st.session_state.messages)
                st.session_state.messages.append(AIMessage(content=response.content))

            # 通常のチャット入力
            if user_input := st.chat_input(input_hint):
                st.session_state.messages.append(HumanMessage(content=user_input))
                with st.spinner("Loading..."):
                    response = llm(st.session_state.messages)
                st.session_state.messages.append(AIMessage(content=response.content))

            # チャット履歴の表示
            for idx, message in enumerate(messages):
                if idx == 0:  # 最初のメッセージはスキップ
                    continue
                if isinstance(message, AIMessage):
                    with st.chat_message('assistant'):
                        st.markdown(message.content)
                elif isinstance(message, HumanMessage):
                    with st.chat_message('user'):
                        st.markdown(message.content)
        else:
            st.warning('まずは設定を行いましょう！', icon="⚠️")
    else:
        st.session_state.messages.append(HumanMessage(content=
            """今までのやり取りをもとに、下記の項目の観点で面接を採点してください。
            ## 面接官が面接で就活生を評価する際の項目
            1. **総合評価**: 面接の総合点とどの程度この人材を採用したいと思うか
            2. **積極性**: 被面接者は質問に対してどの程度積極的な姿勢を見せたか
            3. **言葉遣い**: 被面接者の言葉遣いは適切だったか
            4. **態度**: 論理性のある回答ができているか"""
        ))
        with st.spinner("Loading..."):
            response = llm(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))
        st.session_state.isScoring = False  # 修正：採点が終了したらFalseに設定

        # 採点モードでは最後のAIメッセージのみを表示
        if len(st.session_state.messages) > 0 and isinstance(st.session_state.messages[-1], AIMessage):
            with st.chat_message('assistant'):
                st.markdown(st.session_state.messages[-1].content)
