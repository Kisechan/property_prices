# -*- coding: UTF-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import matplotlib
import pandas as pd
from matplotlib.font_manager import FontProperties

a=sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
plt.rcParams['font.family'] = 'SimHei'
plt.style.use('ggplot')
fig, axes = plt.subplots(2, 3, figsize=(14, 6))

def draw_area_number():
    cnt = [0 for _ in range(20)]
    for i in range(1, df.index.size):
        if int(df.iat[i, 5]) >= 200:
            continue
        cnt[(int(df.iat[i, 5]) // 10)] += 1

    bins = list(range(0, 210, 10))
    axes[0][0].hist(np.repeat(bins[:-1], cnt), bins=bins, edgecolor='black', alpha=0.7)
    axes[0][0].set_xticks(bins, [f'{x}' for x in bins])
    axes[0][0].set_title("房屋面积分布")
    axes[0][0].set_xlabel("面积")
    axes[0][0].set_ylabel("数量")

def draw_area_averageattention():
    cnt = [0 for _ in range(20)]
    num = [0.0 for _ in range(20)]
    for i in range(1, df.index.size):
        if int(df.iat[i, 5]) >= 200:
            continue
        cnt[(int(df.iat[i, 5]) // 10)] += 1
        num[(int(df.iat[i, 5]) // 10)] += df.iat[i,13]
    for i in range(20):
        if (cnt[i]==0):
            continue
        num[i]=1.0*num[i]/cnt[i]

    bins = list(range(0, 210, 10))
    axes[1][0].bar(bins[:-1], num, width=10, edgecolor='black', alpha=0.7)
    axes[1][0].set_xticks(bins, [f'{x}' for x in bins])
    #axes[1].gca().yaxis.set_major_formatter(FormatStrFormatter('%.4f'))
    axes[1][0].set_title("房屋面积平均关注分布")
    axes[1][0].set_xlabel("面积 (平米)")
    axes[1][0].set_ylabel("平均关注")

def draw_number_price():
    cnt = [0 for _ in range(16)]
    for i in range(1, df.index.size):
        if int(df.iat[i, 12]) >= 16000:
            continue
        cnt[(int(df.iat[i, 12]) // 1000)] += 1

    bins = list(range(0, 17000, 1000))
    axes[0][1].hist(np.repeat(bins[:-1], cnt),color="deepskyblue", bins=bins, edgecolor='black', alpha=0.7)
    axes[0][1].set_xticks(bins, [f'{x//1000}k' for x in bins])
    axes[0][1].set_title("房屋单价分布")
    axes[0][1].set_xlabel("单价")
    axes[0][1].set_ylabel("数量")

def draw_price_averageattention():
    cnt = [0 for _ in range(16)]
    num = [0.0 for _ in range(16)]
    for i in range(1, df.index.size):
        if int(df.iat[i, 12]) >= 16000:
            continue
        cnt[(int(df.iat[i, 12]) // 1000)] += 1
        num[(int(df.iat[i, 12]) // 1000)] += df.iat[i,13]
    for i in range(16):
        if (cnt[i]==0):
            continue
        num[i]=1.0*num[i]/cnt[i]

    bins = list(range(0, 17000, 1000))
    axes[1][1].bar(bins[:-1], num, width=1000, color="deepskyblue",edgecolor='black', alpha=0.7)
    axes[1][1].set_xticks(bins, [f'{x//1000}k' for x in bins])
    #axes[1].gca().yaxis.set_major_formatter(FormatStrFormatter('%.4f'))
    axes[1][1].set_title("房屋单价平均关注分布")
    axes[1][1].set_xlabel("单价")
    axes[1][1].set_ylabel("平均关注")

def draw_floor_cnt():
    cnt_low = [0 for _ in range(10)]
    cnt_mid = [0 for _ in range(10)]
    cnt_high= [0 for _ in range(10)]
    bt2=[0 for _ in range(10)]
    for i in range(1, df.index.size):
        if df.iat[i,9]=="未知数据":
            continue
        if int(df.iat[i, 9]) >= 38:
            continue
        if df.iat[i,8]=="高楼层":
            cnt_high[(int(df.iat[i, 9])+2) // 4]+=1
        elif df.iat[i,8]=="中楼层":
            cnt_mid[(int(df.iat[i, 9])+2) // 4]+=1
        elif df.iat[i,8]=="低楼层":
            cnt_low[(int(df.iat[i, 9])+2) // 4]+=1
    for i in range(10):
        bt2[i]=cnt_low[i]+cnt_mid[i]

    bins = list(range(0, 44, 4))
    axes[0][2].bar(bins[:-1], cnt_low, width=4, edgecolor='black', alpha=0.7, label="低楼层")
    axes[0][2].bar(bins[:-1], cnt_mid, width=4, edgecolor='black', alpha=0.7, bottom=cnt_low,label="中楼层")
    axes[0][2].bar(bins[:-1], cnt_high, width=4, edgecolor='black', alpha=0.7, bottom=bt2, label="高楼层")
    axes[0][2].set_xticks(bins, [f'{x}' for x in bins])
    axes[0][2].set_title("房屋楼层分布")
    axes[0][2].set_xlabel("楼层数")
    axes[0][2].set_ylabel("数量")
    axes[0][2].legend()

def draw_floor_averageattention():
    cnt_low = [0 for _ in range(10)]
    cnt_mid = [0 for _ in range(10)]
    cnt_high = [0 for _ in range(10)]
    bt2 = [0 for _ in range(10)]
    num_low = [0 for _ in range(10)]
    num_mid = [0 for _ in range(10)]
    num_high= [0 for _ in range(10)]
    for i in range(1, df.index.size):
        if df.iat[i, 9] == "未知数据":
            continue
        if int(df.iat[i, 9]) >= 38:
            continue
        if df.iat[i, 8] == "高楼层":
            cnt_high[(int(df.iat[i, 9]) + 2) // 4] += 1
            num_high[(int(df.iat[i, 9]) + 2) // 4] += df.iat[i,13]
        elif df.iat[i, 8] == "中楼层":
            cnt_mid[(int(df.iat[i, 9]) + 2) // 4] += 1
            num_mid[(int(df.iat[i, 9]) + 2) // 4] += df.iat[i, 13]
        elif df.iat[i, 8] == "低楼层":
            cnt_low[(int(df.iat[i, 9]) + 2) // 4] += 1
            num_low[(int(df.iat[i, 9]) + 2) // 4] += df.iat[i, 13]

    for i in range(10):
        if cnt_high[i]==0:
            continue
        num_high[i]=1.0*num_high[i]/cnt_high[i]
        if cnt_mid[i]==0:
            continue
        num_mid[i] = 1.0 * num_mid[i] / cnt_mid[i]
        if cnt_low[i]==0:
            continue
        num_low[i] = 1.0 * num_low[i] / cnt_low[i]
        bt2[i]=num_low[i]+num_mid[i]

    bins = list(range(0, 44, 4))
    axes[1][2].bar(bins[:-1], num_low, width=4, edgecolor='black', alpha=0.7, label="低楼层")
    axes[1][2].bar(bins[:-1], num_mid, width=4, edgecolor='black', alpha=0.7, bottom=num_low, label="中楼层")
    axes[1][2].bar(bins[:-1], num_high, width=4, edgecolor='black', alpha=0.7, bottom=bt2, label="高楼层")
    axes[1][2].set_xticks(bins, [f'{x}' for x in bins])
    axes[1][2].set_title("房屋楼层平均关注分布")
    axes[1][2].set_xlabel("楼层数")
    axes[1][2].set_ylabel("平均关注")
    axes[1][2].legend()

df=pd.read_excel("dataprocessed.xls")
draw_area_number()
draw_area_averageattention()
draw_number_price()
draw_price_averageattention()
draw_floor_cnt()
draw_floor_averageattention()
plt.tight_layout()
plt.show()

