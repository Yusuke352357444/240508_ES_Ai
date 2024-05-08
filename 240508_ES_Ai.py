import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import streamlit as st
import google.generativeai as genai

api_key = st.secrets["gemini_api_key"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title='ES添削ツール', layout='wide')
col1, col2 = st.columns([1, 20])
with col1: st.image('', width=100)

st.markdown("""
<style>
body {
font-family: 'Arial', sans-serif;
background-color: #b0c4de;
color: #333;
}
.stRadio > label {
display: inline-block;
background-color: #FFFFFF;
color: #333;
border-radius: 10px;
}
.stTextArea > div > div > textarea {
background-color: #FFFFFF;
border-color: #CCCCCC;
}

</style>
""", unsafe_allow_html=True)

industry = st.text_input("業界と業種を入力してください（片方だけでも可）", "", placeholder="広告業界・人材業界｜営業職・事務職")


content_type = st.radio(
"添削内容選択",
options=['自己PR', '志望動機', 'ガクチカ', '長所短所'],
horizontal=True
)

content = st.text_area("こちらに内容を入力してください", height=300)


if st.button('添削する'):
 if content:
   question_text = f"{industry}の{content_type}として、以下の内容を添削してください。\n\n点数100点満点中採点をして、改善案を３つ提示してその改善案を反映した{content_type}を教えてください。\n\n{content}。"
   response = model.generate_content(question_text)
   improved_text = response.text
   char_count = len(improved_text)
   st.write("添削結果:", improved_text)
   st.write("文字数:", char_count)
st.error('内容を入力してください。')