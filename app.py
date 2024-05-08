import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import streamlit as st
import google.generativeai as genai

# APIキーの設定
api_key = st.secrets["gemini_api_key"]
genai.configure(api_key=api_key)

# モデルの設定
model = genai.GenerativeModel('gemini-pro')

# タイトル
st.title('自己PRジェネレータ')

# ユーザー入力
industry_or_occupation = st.text_input("志望する業界または業種を教えてください　例ー広告業界、営業、事務（任意）")
mbti_result = st.text_input("MBTI診断結果を教えてください　例ーISFJ、ESFP（任意）")
strengths_and_abilities = st.text_input("強みと能力を教えてください（必須）")
achievements = st.text_input("成果を教えてください（必須）")
experiences = st.text_input("エピソードを教えてください（必須）")

if st.button('自己PRを生成'):
    # テキスト生成
    pr_template = """以下はESに書く自己PRを作成してもらう為の情報です。{industry}と{mbti}タイプの性格特性の業界や業種と性格特性は自己PRには書かず、精度の高い自己PRを作るのに活用してください。私の強みは{strengths}です。これまでに{achievements}の成果を達成し、{experiences}という経験もあります。これらの経験から、私は{industry}での新しいチャレンジにどのように貢献できるかを見出しています。私のスキルと経験が貴社の要求にどのようにマッチするかを詳しく説明した自己PRを作成して。"""

    question_text = pr_template.format(
        industry=industry_or_occupation,
        mbti=mbti_result,
        strengths=strengths_and_abilities,
        achievements=achievements,
        experiences=experiences
    )

    response = model.generate_content(question_text)
    st.write("生成された自己PR:", response.text)
