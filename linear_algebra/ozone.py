import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 미분함수를 다른 파일에 갖다 두고 사용

url = "https://github.com/cs109/2014_data/blob/master/countries.csv"
#s = requests.get(url).content
c = pd.read_csv(url)
# Simple Linear Regression
# 온도에 따른 오존량 예측

class Solution(object):
    def __init__(self):
        # 4. 미분함수
        def numerical_derivative(self, f, x):
            # f : 미분하려고 하는 다변수 함수
            # x : 모든 변수를 포함하고 있는 ndarray
            delta_x = 1e-4
            # 미분한 결과를 저장할 ndarray
            derivative_x = np.zeros_like(x)

            # iterator를 이용해서 입력된변수 x들 각각에 대해 편미분 수행
            it = np.nditer(x, flags=['multi_index'])

            while not it.finished:
                idx = it.multi_index  # iterator의 현재 index를 tuple 형태로 추출

                # 현재 칸의 값을 잠시 저장
                tmp = x[idx]

                x[idx] = tmp + delta_x
                fx_plus_delta = f(x)  # f(x + delta_x)

                x[idx] = tmp - delta_x
                fx_minus_delta = f(x)  # f(x - delta_x)

                # 중앙치분방식
                derivative_x[idx] = (fx_plus_delta - fx_minus_delta) / (2 * delta_x)

                # 데이터 원상 복구
                x[idx] = tmp

                it.iternext()

            return derivative_x


# 1. Raw Data Loading
df = pd.read_csv('./data/ozone.csv')

# 2. Data Preprocessing(데이터 전처리)
# 필요한 column(Temp, Ozone)만 추출
training_data = df[['Temp', 'Ozone']]

# 결측치 제거 - dropna() 함수 이용
training_data = training_data.dropna(how='any')

# 3. Training Data Set
x_data = training_data['Temp'].values.reshape(-1, 1)
t_data = training_data['Ozone'].values.reshape(-1, 1)

# 4. Simple Linear Regression 정의
W = np.random.rand(1, 1)
b = np.random.rand(1)


# 5. loss function 정의
def loss_func(x, t):
    y = np.dot(x, W) + b
    return np.mean(np.power((t - y), 2))  # 최소제곱법


# 6. 학습종료 후 예측값 계산 함수
def predict(x):
    return np.dot(x, W) + b


# 7. 프로그램에서 필요한 변수들 정의
learning_rate = 1e-5
f = lambda x: loss_func(x_data, t_data)

# 8. 학습 진행
for step in range(90000):
    W -= learning_rate * numerical_derivative(f, W)
    b -= learning_rate * numerical_derivative(f, b)

    if step % 9000 == 0:
        print('W : {}, b : {}, loss : {}'.format(W, b, loss_func(x_data, t_data)))

# 9. 예측
result = predict(62)
print(result)  # [[34.56270003]]

# 10. 그래프로 확인
plt.scatter(x_data, t_data)
plt.plot(x_data, np.dot(x_data, W) + b, color='r')
plt.show()

### 결과 ###
# W : [[0.40272539]], b : [0.65852824], loss : 1021.0133992588328
# W : [[0.56489002]], b : [0.27553638], loss : 867.0867878634871
# W : [[0.56974644]], b : [-0.1081987], loss : 865.4504172415336
# W : [[0.57459021]], b : [-0.49093391], loss : 863.822563090739
# W : [[0.57942136]], b : [-0.87267184], loss : 862.203181087224
# W : [[0.58423992]], b : [-1.25341511], loss : 860.5922271378048
# W : [[0.58904593]], b : [-1.63316629], loss : 858.9896573787686
# W : [[0.59383941]], b : [-2.01192798], loss : 857.3954281746938
# W : [[0.5986204]], b : [-2.38970275], loss : 855.8094961172706
# W : [[0.60338894]], b : [-2.76649318], loss : 854.231818024095

if __name__ == '__main__':
    Solution().solution()