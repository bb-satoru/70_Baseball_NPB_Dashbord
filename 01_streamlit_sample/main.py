import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px



st.title("2020年の野手成績を振り返る")


st.write("DetaFrame")
### サイドバー ###
st.sidebar.write("サイドバー")


main.py

uploaded_file = st.sidebar.file_uploader("ファイルアップロード", type='csv') 

# メイン画面
st.header('読み込みデータ表示')
if uploaded_file is not None:
    # アップロードファイルをメイン画面にデータ表示
    df = pd.read_csv(uploaded_file)

    st.dataframe(df.style.highlight_max(axis = 0))
#df = pd.read_csv("test_batting.csv")
#st.dataframe(df.style.highlight_max(axis = 0))
    x_ = st.sidebar.selectbox("x軸を決めてください",df.columns)
    y_ = st.sidebar.selectbox("y軸を決めてください",df.columns)
    bouble = st.sidebar.selectbox("バブルサイズを決めてください",df.columns)
    games = st.sidebar.text_input("打席数を決めてください:", 0)
##################

if st.sidebar.button("決定"):
    df = df[df.Plate_Appearances > int(games)]
    fig = px.scatter(df, x=x_, y=y_, size = bouble,color="Team_Name",hover_name = "Player_Name",
     size_max=30)
    st.plotly_chart(fig, use_container_width=True)

    df = df[df.Plate_Appearances > int(games)]
    fig = px.scatter(df, x=x_, y=y_, size = bouble,hover_name = "Player_Name",
     size_max=30, trendline="ols", marginal_x="histogram", marginal_y="rug")
    #fig = px.scatter(x=df[x_], y=df[y_], x=x_, y=y_)
    st.plotly_chart(fig, use_container_width=True)


####################################

# streamlit run main.py
