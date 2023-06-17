import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# CSV 파일 로드
data = pd.read_csv('model/data.csv')

# 특성과 타겟 분리
X = data.drop('war', axis=1)
y = data['war']

# 학습 및 테스트 데이터셋 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# RandomForest 회귀 모델 훈련
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# 테스트 데이터셋에 대한 예측
y_pred = model.predict(X_test)

# 평균 제곱 오차 계산
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)
print('R2 Score:', r2_score(y_test, y_pred))

# 학습된 모델링 부호화(pickle)
with open('model/model.pkl','wb') as pickle_file:
    pickle.dump(model, pickle_file)


