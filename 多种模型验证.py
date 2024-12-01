import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.metrics import r2_score, mean_squared_error



filename = 'updated.xlsx'
featCols = ['所属地区', '户型', '面积', '朝向', '装潢', '楼层高低', '总楼层数', '建筑类型']
targetCols = ['单价']



def inputData():
    data = pd.read_excel(filename, usecols = featCols + targetCols, engine='openpyxl')
    return data

def onehotPre(data):                    # 独热编码，适合类少的数据
    types = data[['楼层高低', '建筑类型']]
    types_encoded = pd.get_dummies(types, drop_first=True)
    return types_encoded

def averagePre(df, feature, target):    # 平均值编码
    encoding_map = df.groupby(feature)[target].mean()
    return df[feature].map(encoding_map)

def preData(data):                      # 预处理
    fr_data = data[['面积', '总楼层数']]
    oh_data = onehotPre(data)
    dc_data = averagePre(data, '所属地区', '单价')
    ht_data = averagePre(data, '户型', '单价')
    ft_data = averagePre(data, '朝向', '单价')
    de_data = averagePre(data, '装潢', '单价')
    final_data = pd.concat([fr_data, oh_data, dc_data, ht_data, ft_data, de_data], axis=1)
    # print(final_data.head())
    # 将所有的数据粘合成一个DataFrame
    return final_data




def main():
    data = inputData()
    final_data = preData(data)
    X = final_data.values
    y = data[targetCols].values.ravel()


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6, random_state=400)

    scaler = StandardScaler()   # 数据标准化，转化成正态分布
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    models = {
        'K-邻近算法': KNeighborsRegressor(),
        '线性回归': LinearRegression(),
        '岭回归': Ridge(),
        '拉索回归': Lasso(),
        '决策树回归': DecisionTreeRegressor(),
        '支持向量回归': SVR()
    }

    for name, model in models.items():              # 每个模型都试一遍
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)               # r2值
        mse = mean_squared_error(y_test, y_pred)    # 均方根误差

        print(f"模型 {name} 的 r2 值为：{r2:.4f}，RMSE 值为 {np.sqrt(mse):.4f}")

        R = random.randrange(0, len(X_test))  # 取随机数
        y_true = y_test[R]
        X_sample = X_test[R].reshape(1, -1)         # 转置向量

        y_pred_sample = model.predict(X_sample)
        print(f'房价真实值为：{y_true:.2f}，房价推测值为：{y_pred_sample[0]:.2f}，差值为：{abs(y_pred_sample[0] - y_true):.2f}\n')

    print("综合以上，可以看到线性回归、岭回归、拉索回归的效果是最好的")

if __name__ == '__main__':
    main()
