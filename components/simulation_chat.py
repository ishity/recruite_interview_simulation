from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage
from dotenv import load_dotenv
import os
import streamlit as st

def simulation(situation):
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    
    llm = ChatOpenAI(temperature=0, openai_api_key=api_key)

    input_hint = ""
    if "就活生" in situation:
        input_hint = "就活生に質問しよう！"
    else:
        input_hint = "面接官の質問に答えよう！"

    if st.session_state.first_input != "":
        # if st.button("リセット"):
        #     st.session_state.messages = []

        # 1メッセージ目を送る
        if st.session_state.messages == []:
            st.session_state.messages.append(HumanMessage(content=st.session_state.first_input))
            with st.spinner("Loading..."):
                response = llm(st.session_state.messages)
            st.session_state.messages.append(AIMessage(content=response.content))

        if user_input := st.chat_input(input_hint):
            st.session_state.messages.append(HumanMessage(content=user_input))
            with st.spinner("Loading..."):
                response = llm(st.session_state.messages)
            st.session_state.messages.append(AIMessage(content=response.content))

        # チャット履歴の表示
        messages = st.session_state.get('messages', [])
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

