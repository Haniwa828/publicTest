import streamlit as st
import time

st.title('Streamlitt 超入門')
st.write('Progressbar')


# プログレスバーの用意
latest_interation = st.empty() # 空要素だけど先に書いておくことで後で要素を入れてもバーより上に出現
bar = st.progress(0)

for i in range(100): # 0-99
    latest_interation.text(f'Interation {i + 1}') # 空だった要素のテキストを動かす
    bar.progress(i + 1) # バーを進める
    time.sleep(0.1) # 0.1秒停止

# これ以下は上のが終了したら読み込まれる
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander.text_input('記述欄')