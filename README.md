# streamlit-medical-insurance-cost
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![streamlit](https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png)

[http://ec2-3-35-26-163.ap-northeast-2.compute.amazonaws.com:8502/](http://ec2-3-35-26-163.ap-northeast-2.compute.amazonaws.com:8502/)

보험비에 영향을 미치는 요소들을 시각화 해보고 보험비를 예측하는 앱입니다.

데이터 출처 kaggle

![사진](https://i.imgur.com/zTnvOcb.jpg)

# 데이터셋

* age 나이
* sex 성별
* bmi bmi
* children 자녀수
* smoker 흡연여부
* region 지역
* charges 보험비

# 분석

* plotly를 통해서 각 요소의 분포 시각화
* 각 요소별로 구분지어서 보험비 분포 시각화 

# 보험비 예측

* 각 요소들을 입력했을 때 RandomForestRegressor로 보험비 예측
