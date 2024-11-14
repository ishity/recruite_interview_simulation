import streamlit as st

def simple_selection(var, text, selection):
    return st.selectbox(
        text,
        options=selection,
        index=selection.index(var)
    )

def simple_selection2(var, text, selection):
    return st.selectbox(
        text,
        options=selection,
        index=selection.index(var) if var in selection else 0
    )

def prompt_setting():
    tab = st.tabs(['面接官へのプロンプト', '就活生へのプロンプト'])
    st.markdown(
            """
            <style>
            /* テキスト入力欄の高さと折り返しを調整 */
            .text-input {
                height: 100px; /* 縦幅を広げる */
                white-space: pre-wrap; /* 折り返しを有効にする */
            }

            /* テキスト表示の上下に余白を追加 */
            .text-display {
                margin-top: 20px;
                margin-bottom: 20px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    with tab[0]:
        # テキスト入力フィールドまたは表示テキスト
        if 'edit_mode' not in st.session_state:
            st.session_state.edit_mode = False

        if st.session_state.edit_mode:
            # テキスト入力フィールドの表示
            st.session_state.prompt1_interviewer = st.text_area(
                "プロンプト", 
                st.session_state.prompt1_interviewer,
                height=100,  # 縦幅を設定
                key="text-input"  # CSSを適用するためのキー
            )
        else:
            # テキスト表示の上下に余白を追加
            st.markdown(f'<div class="text-display">{st.session_state.prompt1_interviewer}</div>', unsafe_allow_html=True)

        # 「プロンプトを修正する」「プロンプトを決定する」ボタンの表示
        if st.button("プロンプトを決定する" if st.session_state.edit_mode else "プロンプトを修正する", key='prompt1_toggle'):
            st.session_state.edit_mode = not st.session_state.edit_mode

        if st.button("リセット", key='prompt1_reset'):
            st.session_state.prompt1_interviewer = 'あなたは面接官としてこれから就活面接を行います。就活生の話した内容をもとに、就活生に対して質問を投げかけてください。ではまずあなたの方から就活生に自己紹介を促してください。'
            st.session_state.edit_mode = False  # リセット時は編集モードをオフに戻す

    with tab[1]:
        # テキスト入力フィールドまたは表示テキスト
        if 'edit_mode2' not in st.session_state:
            st.session_state.edit_mode2 = False

        if st.session_state.edit_mode2:
            # テキスト入力フィールドの表示
            st.session_state.prompt1_student = st.text_area(
                "プロンプト", 
                st.session_state.prompt1_student,
                height=100,  # 縦幅を設定
                key="text-input"  # CSSを適用するためのキー
            )
        else:
            # テキスト表示の上下に余白を追加
            st.markdown(f'<div class="text-display">{st.session_state.prompt1_student}</div>', unsafe_allow_html=True)

        # 「プロンプトを修正する」「プロンプトを決定する」ボタンの表示
        if st.button("プロンプトを決定する" if st.session_state.edit_mode2 else "プロンプトを修正する", key='prompt1_toggle2'):
            st.session_state.edit_mode2 = not st.session_state.edit_mode2

        # リセットボタン
        if st.button("リセット", key='prompt1_reset2'):
            st.session_state.prompt1_student = 'あなたは就活生としてこれから就活面接を行います。面接官の質問に適宜答えてください。ではまず面接官に挨拶をしてください。'
            st.session_state.edit_mode2 = False  # リセット時は編集モードをオフに戻す
