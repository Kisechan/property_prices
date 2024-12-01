import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import cm
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 设置字体
df = pd.read_excel("qing.xlsx")  # 使用pandas读取excel文件
def p_1():#装潢-数量
    plt.figure(figsize=(50, 30))
    x = df['装潢'].value_counts().index.tolist()
    y = df['装潢'].value_counts().values.tolist()
    t = np.arange(4)
    plt.bar(t, height=y, width=0.4, align='center', tick_label=x, color='Aqua', linewidth=2)
    plt.tick_params(axis='both', labelsize=30)
    plt.xlabel('装潢类别', fontsize=50, color='Black')
    plt.ylabel('数量', fontsize=50, color='Black')
    for a, b in zip(t, y):
        plt.text(a, b + 0.1, '%.2f' % b, ha='center', va='center', fontsize=40)
    plt.show()
def p_2():#装潢-单价
    plt.figure(figsize=(50, 30))
    x = df['单价'].groupby(df['装潢']).mean().index.tolist()
    y = df['单价'].groupby(df['装潢']).mean().values.tolist()
    t = np.arange(4)
    plt.bar(t, height=y, width=0.5, align='center', tick_label=x, color='LightSkyBlue')
    plt.tick_params(axis='both', labelsize=30)
    plt.xlabel('装潢类别', fontsize=50, color='Black')
    plt.ylabel('单价（元/平米）', fontsize=50, color='Black')
    for a, b in zip(t, y):
        plt.text(a, b + 0.2, '%.2f' % b, ha='center', va='center', fontsize=40)
    plt.show()
def p_3():#装潢-关注度
    plt.figure(figsize=(50, 30))
    x = df['关注度'].groupby(df['装潢']).mean().index.tolist()
    y = df['关注度'].groupby(df['装潢']).mean().values.tolist()
    t = np.arange(4)
    plt.bar(t, height=y, width=0.5, align='center', tick_label=x, color='Yellow')
    plt.tick_params(axis='both', labelsize=30)
    plt.xlabel('装潢类别', fontsize=50, color='Black')
    plt.ylabel('关注度', fontsize=50, color='Black')
    for a, b in zip(t, y):
        plt.text(a, b + 0.05, '%.2f' % b, ha='center', va='center', fontsize=40)
    plt.show()
def p_4():#地区-数量
    plt.figure(figsize=(50, 30))
    x = df['所属地区'].value_counts().index.tolist()
    y = df['所属地区'].value_counts().values.tolist()
    t = np.arange(len(x))
    plt.barh(t, height=0.5, width=y, align='center', tick_label=x, color='Tomato')
    plt.tick_params(axis='both', labelsize=20)
    plt.xlabel('数量', fontsize=50, color='Black')
    plt.ylabel('所属地区', fontsize=50, color='Black')
    for a, b in zip(y, t):
        plt.text(a + 0.2, b, '%.0f' % a, ha='center', va='center', fontsize=20, color='Black')
    plt.show()
def p_5():#地区-单价
    plt.figure(figsize=(50, 30))
    s = df['单价'].groupby(df['所属地区']).mean()
    e = s.sort_values(ascending=False)
    x = e.index.tolist()
    y = e.values.tolist()
    t = np.arange(len(x))
    plt.barh(t, height=0.4, width=y, align='center', tick_label=x,color='LightCoral')
    plt.tick_params(axis='both', labelsize=20)
    plt.xlabel('单价(元/平米)', fontsize=50, color='Black')
    plt.ylabel('所属地区', fontsize=50, color='Black')
    for a, b in zip(y, t):
        plt.text(a + 0.2, b, '%.2f' % a, ha='center', va='center', fontsize=20, color='Black')
    plt.show()
def p_6():#地区-关注度
    plt.figure(figsize=(50, 30))
    s = df['关注度'].groupby(df['所属地区']).mean()
    e = s.sort_values(ascending=False)
    x = e.index.tolist()
    y = e.values.tolist()
    t = np.arange(len(x))
    plt.barh(t, height=0.4, width=y, align='center', tick_label=x,color='MediumAquamarine')
    plt.tick_params(axis='both', labelsize=20)
    plt.xlabel('关注度', fontsize=50, color='Black')
    plt.ylabel('所属地区', fontsize=50, color='Black')
    for a, b in zip(y, t):
        plt.text(a + 0.1, b, '%.2f' % a, ha='center', va='center', fontsize=20, color='Black')
    plt.show()

p_1()
p_2()
p_3()
p_4()
p_5()
p_6()

