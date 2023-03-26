# streamlit-medical-insurance-cost
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Streamlit](https://img.shields.io/badge/streamlit-FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)

보험비에 영향을 미치는 요소들을 시각화 해보고 보험비를 예측하는 앱입니다.

데이터 출처 [https://www.kaggle.com/datasets/mirichoi0218/insurance](https://www.kaggle.com/datasets/mirichoi0218/insurance)

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
* 컬럼을 선택해서 히스토그램 출력
* 보험비 최대 최소인 행 출력
* 각 요소별로 구분지어서 보험비 분포 시각화 
* 상관관계 시각화

# 보험비 예측

* 각 요소들을 입력했을 때 RandomForestRegressor로 보험비 예측

![다운로드 (2)](https://user-images.githubusercontent.com/105832345/173175876-85883428-ffe6-4c6f-9b76-6d0f92b72a5f.png)

