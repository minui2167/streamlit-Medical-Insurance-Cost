import streamlit as st
import numpy as np
import pandas as pd
import joblib

def run_ml():
    encoder_sex = joblib.load('data/encoder_sex.pkl')
    encoder_smoker = joblib.load('data/encoder_smoker.pkl')
    encoder_region = joblib.load('data/encoder_region.pkl')
    m_scaler = joblib.load('data/m_scaler.pkl')
    rfr = joblib.load('data/rfr.pkl')
    st.subheader('RandomForestRegressor 통해서 예측해보기')

    age = st.number_input('나이', 18, 120, value = 40)
    sex = st.selectbox('성별', ['남자', '여자'])
    bmi = st.number_input('bmi', 10.0, 70.0, value = 30.0)
    children = st.number_input('자녀수', 0)
    region = st.selectbox('지역', ['southwest', 'southeast', 'northwest', 'northeast'])
    smoker = st.checkbox('흡연 여부')

    if sex == '남자':
        sex = 'male'
    else:
        sex = 'female'

    if smoker:
        smoker = 'yes'
    else:
        smoker = 'no'

    if st.button('예측'):
        test = np.array([age, sex, bmi, children, smoker, region])
        test[1] = encoder_sex.transform(pd.Series(test[1]))[0]
        test[4] = encoder_smoker.transform(pd.Series(test[4]))[0]
        test[5] = encoder_region.transform(pd.Series(test[5]))[0]
        test = m_scaler.transform(test.reshape(1, -1))
        st.text('예상 보험비는 '+str(rfr.predict(test)[0].round(4)) + ' 달러 입니다.')