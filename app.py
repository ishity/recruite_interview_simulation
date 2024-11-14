from components.sample_chat import create_samp
from components.simulation_chat import simulation
from components.settings import simple_selection, simple_selection2, prompt_setting
from components.structured_chat import structured_chat
from utils.session_state import init_session_state
import streamlit as st
import pandas as pd

# データの読み込み
data = pd.read_csv("data/persona.csv")  # CSVの場合

st.set_page_config(
    page_title="就活面接対話シミュレーション",
    page_icon="🏢"
)

# 配列
utterance_type = ["面接官と対話", "就活生と対話"]
interviewer = []
student = []
tab = ['就活面接シミュレーション', '構造化面接シミュレーション', '就活面接サンプル', 'プロンプトの設定']

for i in range(len(data)):
    if "interviewer" in data.loc[i, 'category']:
        interviewer.append(data.loc[i, 'name'])
    elif "student" in data.loc[i, 'category']:
        student.append(data.loc[i, 'name'])

# 初期化
init_session_state(utterance_type, interviewer, student, tab)
person = ""
select1 = interviewer[0]
select2 = student[0]

# サイドバー内のコンテンツ
with st.sidebar:
    st.write("就活面接シミュレーション")
    with st.expander("設定"):
        st.session_state.utterance_setting = simple_selection(st.session_state.utterance_setting, "対話形式を選択してください:", utterance_type)
        persona_options = interviewer if st.session_state.utterance_setting == utterance_type[0] else student
        st.session_state.persona_setting = simple_selection2(st.session_state.persona_setting, "誰と対話しますか？:", persona_options)
        if st.button('面接を始める'):
            st.session_state.tab_selected = tab[0]
            st.session_state.messages = []

            rows = data.index[data['name'] == st.session_state.persona_setting].tolist()
            person = data.loc[rows, 'persona']

            # 面接開始後にメッセージを追加
            if "面接官" in st.session_state.utterance_setting:
                st.session_state.first_input = f"あなたは次のような面接官です。{person}。" + st.session_state.prompt1_interviewer
            else:
                st.session_state.first_input = f"あなたは次のような就活生です。{person}。" + st.session_state.prompt1_student

    st.write("構造化面接シミュレーション")
    with st.expander("設定"):
        if st.button('構造化面接を始める'):
            st.session_state.messages = []
            st.session_state.tab_selected = tab[1]

    st.write("就活面接サンプル")
    with st.expander("設定"):
        st.session_state.interviewer_setting = simple_selection(st.session_state.interviewer_setting, "面接官を選択してください:", interviewer)
        st.session_state.student_setting = simple_selection(st.session_state.student_setting, "就活生を選択してください:", student)
        if st.button('サンプルを生成'):
            st.session_state.tab_selected = tab[2]
            st.session_state.messages = []
            if st.session_state.interviewer_setting == "女性面接官":
                select1 = data.loc[0, 'persona']
            else:
                select1 = data.loc[1, 'persona']

            if st.session_state.interviewer_setting == "女性就活生":
                select2 = data.loc[2, 'persona']
            else:
                select2 = data.loc[3, 'persona']

    st.divider()
    st.write("その他の設定")
    if st.button("プロンプトを修正する"):
        st.session_state.tab_selected = tab[3]


# 選択したタブに応じた表示
if st.session_state.tab_selected == tab[0]:
    st.title(tab[0])
    simulation(st.session_state.utterance_setting)
elif st.session_state.tab_selected == tab[1]:
    st.title(tab[1])
    structured_chat()
elif st.session_state.tab_selected == tab[2]:
    st.title(tab[2])
    create_samp(select1, select2)
elif st.session_state.tab_selected == tab[3]:
    st.title(tab[3])
    prompt_setting()