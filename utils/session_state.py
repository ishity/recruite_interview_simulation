import streamlit as st
from langchain.schema import SystemMessage

def init_session_state(utterance_type, interviewer, student, tab):
    ## 就活シミュレーションの変数の初期化
    if "utterance_setting" not in st.session_state:
        st.session_state.utterance_setting = utterance_type[0]

    if "studentetting" not in st.session_state:
        st.session_state.persona_setting = interviewer[0] if st.session_state.utterance_setting == utterance_type[0] else student[0]

    ## 就活面接サンプルの変数の初期化
    if "interviewer_setting" not in st.session_state:
        st.session_state.interviewer_setting = interviewer[0]

    if "student_setting" not in st.session_state:
        st.session_state.student_setting = student[0]

    if 'tab_selected' not in st.session_state:
        st.session_state.tab_selected = tab[0]

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    if 'first_input' not in st.session_state:
        st.session_state.first_input = ''

    if 'prompt1_interviewer' not in st.session_state:
        st.session_state.prompt1_interviewer = 'あなたは面接官としてこれから就活面接を行います。就活生の話した内容をもとに、就活生に対して質問を投げかけてください。ではまずあなたの方から就活生に自己紹介を促してください。'
    
    if 'prompt1_student' not in st.session_state:
        st.session_state.prompt1_student = 'あなたは就活生としてこれから就活面接を行います。面接官の質問に適宜答えてください。ではまず面接官に挨拶をしてください。'