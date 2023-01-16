#streamlitとRandomのインポート
import streamlit as st
import random


#タイトルを書く
st.title("What's for dinner?")

#ご飯の選択肢をリストで表記
menu = ["chicken", "beef", "pork", "tofu", "shrimp", "salmon", "vegetables"]

#ボタンの追加
button = st.button("Pick something")

#選ばれたご飯を表示する
if button:
    choice = random.choice(menu)
    st.write("How about some delicious", choice, "for dinner tonight!")