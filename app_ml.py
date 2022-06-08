import streamlit as st
import numpy as np
import joblib
import plotly.express as px
import pandas as pd

def run_ml():
    # 데이터프레임 ColumnTransformer,MinMaxScaler,RandomForestRegressor 로드
    df = pd.read_csv('data/insurance.csv')
    ct = joblib.load('data/ct.pkl')
    m_scaler = joblib.load('data/m_scaler.pkl')
    rfr = joblib.load('data/rfr.pkl')
    st.subheader('보험비 예측')

    # 조건 입력
    age = st.number_input('나이', 18, 120, value = 40)
    sex = st.selectbox('성별', ['남자', '여자'])
    bmi = st.number_input('bmi', 10.0, 70.0, value = 30.0)
    children = st.number_input('자녀수', 0)
    region = st.selectbox('지역', df['region'].unique())
    smoker = st.checkbox('흡연 여부')

    # 인코딩전 전처리
    if sex == '남자':
        sex = 'male'
    else:
        sex = 'female'

    if smoker:
        smoker = 'yes'
    else:
        smoker = 'no'

    # np.array를 reshape후 전처리하고 예상
    if st.button('예측'):
        test = np.array([age, sex, bmi, children, smoker, region])
        test = test.reshape(1, -1)
        test = ct.transform(test)
        test = m_scaler.transform(test)
        st.text('예상 보험비는 '+str(rfr.predict(test)[0].round(4)) + ' 달러 입니다.')

    # feature들 시각화
    importances = rfr.feature_importances_
    indices = np.argsort(importances)[::-1]
    variables = ['sex', 'smoker', 'region', 'age','bmi', 'children']
    importance_list = []
    for f in range(len(variables)):
        variable = variables[indices[f]]
        importance_list.append(variable)

    st.subheader('feature importances')
    fig = px.bar(x = importance_list, y = importances[indices])
    st.plotly_chart(fig)
    st.text('흡연여부가 제일 중요하며, 다음으로 bmi와 age가 영향을 미친다. 나머지는 별로 안 중요하다.')