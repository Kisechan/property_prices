# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def showFront(df):
    ser=df.groupby('朝向').size()
    plt.pie(ser.values,
            startangle=90,
            textprops={'size': 'smaller'},
            radius=1,
            wedgeprops=dict(width=0.3),
            pctdistance=1.5
            )
    plt.legend(labels=ser.index)
    plt.title("房屋朝向")
    plt.show()

def showFloor(df):
    ser=df.groupby('楼层高低').size()
    plt.pie(ser.values,
            labels=ser.index,
            autopct='%.3f%%',
            startangle=90,
            textprops={'fontsize': 12},
            wedgeprops=dict(width=0.3),
            radius=1
            )
    plt.legend(labels=ser.index)
    plt.title("楼层高低")
    plt.show()

def showType(df):
    ser=df.groupby('建筑类型').size()
    plt.pie(ser.values,
            autopct='%.2f%%',
            startangle=90,
            textprops={'fontsize': 10},
            wedgeprops=dict(width=0.3),
            radius=0.8,
            pctdistance=1.3
            )
    plt.legend(labels=ser.index)
    plt.title("建筑类型")
    plt.show()

# def showDict(df):
#     ser=df.groupby('户型').size()
#     print(len(ser.index))
#     plt.pie(ser.values,
#             autopct='%.2f%%',
#             startangle=90,
#             textprops={'fontsize': 10},
#             wedgeprops=dict(width=0.3),
#             radius=0.8,
#             pctdistance=1.3
#             )
#     plt.legend(labels=ser.index)
#     plt.title("户型")
#     plt.show()

plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.DataFrame(pd.read_excel('updated.xlsx',engine='openpyxl'))


# showFront(df)
# showType(df)
# showFloor(df)
# showDict(df)