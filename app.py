import streamlit as st
from app_eda import run_eda

from app_home import run_home
from app_ml import run_ml
import pandas as pd

def main():
    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴 선택', menu)
    df = pd.read_csv('insurance.csv')
    st.sidebar.subheader('데이터')
    st.sidebar.dataframe(df)
    st.sidebar.subheader('요약')
    st.sidebar.dataframe(df.describe())

    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_eda()
    elif choice == menu[2]:
        run_ml()

if __name__ == '__main__':
    main()