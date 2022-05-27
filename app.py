import streamlit as st
import pandas as pd

from app_eda import run_eda
from app_home import run_home
from app_ml import run_ml


def main():
    st.set_page_config('보험비 분석 및 예측 앱')
    menu = ['Home', '분석', '예측']
    choice = st.sidebar.selectbox('메뉴 선택', menu)
    df = pd.read_csv('data/insurance.csv')
    st.sidebar.subheader('데이터')
    st.sidebar.dataframe(df)

    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_eda()
    elif choice == menu[2]:
        run_ml()

if __name__ == '__main__':
    main()