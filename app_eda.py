import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

def run_eda():
    df = pd.read_csv('data/insurance.csv')
 
    st.subheader('분포 그래프')
    fig = plt.figure()
    sns.set(style='whitegrid')
    selected = st.selectbox('컬럼 선택', df.columns)
    sns.histplot(df[selected], color = 'c')
    st.pyplot(fig)

    st.subheader('보험비 최대와 최소')
    st.dataframe(df.loc[df['charges'] == df['charges'].max()])
    st.text('보험비가 최대인 사람은 나이와 bmi가 평균보다 높으며 흡연자다.')
    st.dataframe(df.loc[df['charges'] == df['charges'].min()])
    st.text('보험비가 최소인 사람은 나이와 bmi가 평균보다 낮으며 비흡연자다.')

    st.subheader('4개의 지역간 차이는 어떻게 될까?')
    fig = plt.figure()
    charges = df['charges'].groupby(df.region).sum().sort_values(ascending = True)
    sns.barplot(charges, charges.index, palette ='Blues')
    st.pyplot(fig)
    st.text('남동부는 50000달러가 넘고 나머지는 40000달러대다.')

    st.subheader('성별간 차이는 얼마나 날까?')
    fig = plt.figure()
    sns.barplot(x ='region', y ='charges', hue = 'sex', data = df, palette ='cool', ci = None)
    st.pyplot(fig)
    st.text('북서부를 빼면 남자가 대체로 더 비싸다.')

    st.subheader('흡연 여부에 따라 얼마나 다를까?')
    fig = plt.figure()
    sns.barplot(x = 'region', y = 'charges', hue='smoker', data=df, palette='Reds_r', ci = None)
    st.pyplot(fig)
    st.text('4개 지역 모두 흡연자가 더 비싸다.')

    st.subheader('자녀수에 따라 얼마나 다를까?')
    fig = plt.figure()
    sns.barplot(x='region', y='charges', hue='children', data=df, palette='Set1', ci = None)
    st.pyplot(fig)
    st.text('뚜렷한 차이는 보이지 않는다.\n')

    st.subheader('흡연 여부에 따른 나이, bmi에 의한 보험비는?')
    fig = sns.lmplot(x = 'age', y = 'charges', data=df, hue='smoker', palette='Set1')
    st.pyplot(fig)
    fig = sns.lmplot(x = 'bmi', y = 'charges', data=df, hue='smoker', palette='Set2')
    st.pyplot(fig)
    st.text('흡연 여부가 중요하며 나이,bmi는 보험비와 약한 양의 상관관계를 보인다.')

    encoder_sex = joblib.load('data/encoder_sex.pkl')
    encoder_smoker = joblib.load('data/encoder_smoker.pkl')
    encoder_region = joblib.load('data/encoder_region.pkl')
    df['sex'] = encoder_sex.fit_transform(df['sex'])
    df['smoker'] = encoder_smoker.fit_transform(df['smoker'])
    df['region'] = encoder_region.fit_transform(df['region'])
    st.subheader('레이블 인코딩 후 상관계수는?')
    fig = plt.figure()
    sns.heatmap(df.corr(), annot=True, cmap=sns.color_palette("YlGnBu", 10))
    st.pyplot(fig)
    st.text('흡연 여부가 보험비와 강한 양의 상관관계를 보인다.')
