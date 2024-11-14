from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage
from dotenv import load_dotenv
import os
import streamlit as st

def create_samp(person1, person2):

    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')

    llm = ChatOpenAI(temperature=0, openai_api_key=api_key)
    
    input = f"""
            # 会話シナリオ

            就活生と面接官が、採用面接を行っているやり取りを再現してください。

            ## キャラクター設定
            - 面接官: {person1}
            - 就活生: {person2}

            ## 面接官が面接で就活生を評価する際の項目
            1. **総合評価**: 面接の総合点とどの程度この人材を採用したいと思うか
            2. **積極性**: 被面接者は質問に対してどの程度積極的な姿勢を見せたか
            3. **言葉遣い**: 被面接者の言葉遣いは適切だったか
            4. **態度**: 論理性のある回答ができているか

            ## 面接官が就活生を評価するために質問する内容
            - 1分程度での自己紹介
            - 大学時代、最も力をいれたことについて
            - これまでに苦労した、または大変だったことについて。また、それをどう乗り越えたのか
            - 現在の卒業論文のテーマについて（まだ卒業論文のテーマが決まっていなければ、大学での得意科目について）
            - 就職活動における仕事選びの軸について
            - 志望業界について、そう考えた理由やきっかけ
            - 第一希望の会社と、その志望動機
            - その「第一志望」の会社に入社したとして、入社後やってみたい仕事
            - 強みについて、その理由や経験
            - 弱みについて、その理由や経験
            - 周囲の人から、どのような人だと言われるか。また、そう言われる理由について
            - チームの中でどのような役割を果たすことが多いか。また、そう考える理由やエピソードについて
            - 対人関係で大切にしていること
            """

    # 1つ目の質問を追加
    st.session_state.messages.append(HumanMessage(content=input))

    # レスポンスをGPTに送信
    with st.spinner("サンプルを作成しています..."):
        response = llm(st.session_state.messages)
    
    # GPTのレスポンスを表示
    st.session_state.messages.append(AIMessage(content=response.content))

    # チャット履歴の表示
    messages = st.session_state.get('messages', [])
    st.markdown(messages[1].content)
