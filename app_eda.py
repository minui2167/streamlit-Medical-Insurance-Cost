import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

def run_eda():
    df = pd.read_csv('data/insurance.csv')
 
    st.subheader('분포 그래프')
    selected = st.selectbox('컬럼 선택', df.columns)
    fig = px.histogram(df, x = selected) 
    st.plotly_chart(fig)

    st.subheader('보험비 최대와 최소')
    st.dataframe(df.loc[df['charges'] == df['charges'].max()])
    st.text('보험비가 최대인 사람은 나이와 bmi가 평균보다 높으며 흡연자다.')
    st.dataframe(df.loc[df['charges'] == df['charges'].min()])
    st.text('보험비가 최소인 사람은 나이와 bmi가 평균보다 낮으며 비흡연자다.')

    st.subheader('4개의 지역간 차이는 어떻게 될까?')
    fig = px.histogram(df, x = "region", y = "charges", color = 'region', barmode = 'group', histfunc = 'avg')
    st.plotly_chart(fig)
    st.text('남동부가 가장 비싸고 남서부가 가장 싸다.')

    st.subheader('성별간 차이는 얼마나 날까?')
    fig = px.histogram(df, x = "region", y = "charges", color = 'sex', barmode = 'group', histfunc = 'avg')
    st.plotly_chart(fig)
    st.text('북서부를 빼면 남자가 대체로 더 비싸다.')

    st.subheader('흡연 여부에 따라 얼마나 다를까?')
    fig = px.histogram(df, x = "region", y = "charges", color = 'smoker', barmode = 'group', histfunc = 'avg')
    st.plotly_chart(fig)
    st.text('4개 지역 모두 흡연자가 더 비싸다.')

    st.subheader('자녀수에 따라 얼마나 다를까?')
    fig = px.histogram(df, x = "region", y = "charges", color = df.sort_values(by = 'children')['children'], barmode = 'group', histfunc = 'avg')
    st.plotly_chart(fig)
    st.text('뚜렷한 차이는 보이지 않는다.\n')

    st.subheader('흡연 여부에 따른 나이, bmi에 의한 보험비는?')
    fig = px.scatter(df, x = "age", y = "charges", color = "smoker")
    st.plotly_chart(fig)
    fig = px.scatter(df, x = "bmi", y = "charges", color = "smoker")
    st.plotly_chart(fig)
    st.text('흡연 여부가 중요하며 나이,bmi는 보험비와 약한 양의 상관관계를 보인다.')

    ct = joblib.load('data/ct.pkl')
    X = ct.transform(df)
    df_corr1 = pd.DataFrame(X)
    df_corr2 = pd.DataFrame(df['charges'])
    df_corr = df_corr1.join(df_corr2)
    df_corr.columns = ['sex', 'smoker', 'region', 'age', 'bmi', 'children', 'charges']
    st.subheader('인코딩 후 상관계수는?')
    fig = px.imshow(df_corr.corr())
    st.plotly_chart(fig)
    st.text('흡연 여부가 보험비와 강한 양의 상관관계를 보인다.')
    print(df_corr.corr())
