import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda():
    df = pd.read_csv('insurance.csv')
 
    st.subheader('연간 보험비 분포 그래프')
    fig = plt.figure()
    sns.set(style='whitegrid')
    sns.histplot(df['charges'], kde = True, color = 'c')
    plt.title('Distribution of Charges')
    st.pyplot(fig)
    st.text('10000달러 이하가 많고 20000달러 이상은 적다.')

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
