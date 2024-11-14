from st_on_hover_tabs import on_hover_tabs
import streamlit as st

# def render_sidebar():
#     with st.sidebar:
#         tabs = on_hover_tabs(tabName=['就活面接シミュレーション', '就活面接サンプル'], iconName=['dashboard', 'money'], default_choice=0)
#     return tabs

# def render_sidebar():
#     with st.sidebar:
#         tabs = on_hover_tabs(tabName=['就活面接シミュレーション', '就活面接サンプル'],
#                             iconName=['dashboard', 'money'],
#                             styles = {'navtab': {'background-color':'#111',
#                                                 'color': '#818181',
#                                                 'font-size': '18px',
#                                                 'transition': '.3s',
#                                                 'white-space': 'nowrap',
#                                                 'text-transform': 'uppercase'},
#                                     'tabStyle': {':hover :hover': {'color': 'red',
#                                                                     'cursor': 'pointer'}},
#                                     'tabStyle' : {'list-style-type': 'none',
#                                                     'margin-bottom': '30px',
#                                                     'padding-left': '30px'},
#                                     'iconStyle':{'position':'fixed',
#                                                 'left':'7.5px',
#                                                 'text-align': 'left'},
#                                     },
#                             key="1")
#     return tabs

def render_sidebar(com1, com2):
    with st.sidebar:
        st.write("就活面接シミュレーション")
        com1
        # expander1 = st.expander('設定')
        # expander1.com1
        # expander1.button('面接を始める')

        st.write("就活面接サンプル")
        com2
        # expander2 = st.expander('設定')
        # expander2.com2
        # expander2.button('サンプルを生成')

        tabs = "就活面接シミュレーション"
        # tabs = on_hover_tabs(tabName=['就活面接シミュレーション', '就活面接サンプル'], iconName=['dashboard', 'money'], default_choice=0)