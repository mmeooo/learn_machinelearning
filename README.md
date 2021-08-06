# test_machinelearning


1. 정보(데이터)단계
  - dropna : info(), describe()  
  - fillna, replace : describe(), value_counts()
  - 컬럼 분류 : 연속형, 분류형 -> 소숫점이 있으면 연속형
  - 시각화 : 통계
  - 정규화 : standard scaler 
    - `scaler = preprocessing.StandardScaler()`, `scaler.fit()`, `scaler.transform()`
    - `lr = LinearRegression()`, `lr.fit(X,Y)`, `lr.score(X,Y)`
  - one-hot encoding: get_dummies
    - 문자를 숫자로 바꾸어 주는 방법 중 하나로 One-Hot Encoding이 있다. 가변수(dummy variable)로  만들어주는 것인데, 이는 0과 1로 이루어진 열을 나타낸다. 1은 있다, 0은 없다를 나타낸다.
  - data split



2. 교육 단계
  - model make & learning
  - check score



3. 서비스 단계
  - pickle:  model save & load, dump
  - receive data 
  - predict
