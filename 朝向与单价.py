import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

ershou=pd.read_excel("qingxi.xlsx")

towards_perprice=ershou[["朝向","单价"]]

tongji=ershou['单价'].groupby(ershou['朝向']).describe() #统计
tongji1=ershou.groupby("朝向")["单价"].mean()


plt.title("朝向与单价关系图",fontsize=40)
plt.xlabel("朝向",fontsize=15)
plt.ylabel("单价",fontsize=15)
# plt.grid(ls="--", alpha=0.5)
#
# plt.bar(tongji1.index,tongji1.values,width=0.5)
# plt.show()


x = np.arange(len(tongji.index.tolist()))
width = 0.3

mean_x = x
middle_x= x + width
std_x  = x + 2 * width

plt.xticks(x+width, labels=tongji.index.tolist())
plt.grid(ls="--", alpha=0.5)
plt.bar(mean_x, tongji["mean"], width=width, color="skyblue", label="平均值")
plt.bar(middle_x, tongji["50%"], width=width, color="saddlebrown", label="中位数")
plt.bar(std_x, tongji["std"], width=width, color="silver", label="标准差")

for i in range(len(tongji.index.tolist())):
    plt.text(mean_x[i],tongji["mean"][i], format(tongji["mean"][i], '.2f'),va="bottom",ha="center",rotation=15,fontsize=7)
    plt.text(middle_x[i],tongji["50%"][i], format(tongji["50%"][i], '.2f'),va="bottom",ha="center",rotation=15,fontsize=6)
    plt.text(std_x[i],tongji["std"][i], format(tongji["std"][i], '.2f'),va="bottom",ha="center",rotation=15,fontsize=6)
plt.legend()

plt.legend()
plt.show()