import streamlit as st
import pandas as pd

def run_home():
    # 제목
    st.subheader('의료 보험비에 영향을 미치는 요소들과 보험비 예상')

    # 이미지 출력
    url = 'https://i.imgur.com/zTnvOcb.jpg'   
    st.image(url)

    # 텍스트
    st.text('나이, 성별, bmi, 자녀수, 흡연 여부, 지역에 따라 보험비(달러)는 어떻게 다를까요?\n위 요소들에 따라 보험비를 예측해 봅시다.')

    # 데이터 전체
    df = pd.read_csv('data/insurance.csv')
    st.subheader('데이터 미리보기')
    st.dataframe(df)

    # describe 요약
    st.subheader('수치형 데이터 요약')
    st.dataframe(df.describe())