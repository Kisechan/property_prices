# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

column_names = ['概况','小区名','所属地区','户型','面积','朝向','装潢','楼层高低','总楼层数','建筑类型','总价','单价','关注度','发布时间','图片地址']
iris_data = pd.read_csv('qingxi.csv', names=column_names, header=0, encoding='utf-8')
iris_data.head()
df=pd.DataFrame(iris_data)
grouped = df.groupby('所属地区').agg({        #限定所属地区
    '关注度': ['min', 'mean', 'max']          #面积 总楼层数 总价 单价 关注度等等均可替换
})
matplotlib.rcParams['font.family'] = 'SimHei'
# 重新格式化数据以便于绘图
grouped.columns = ['Min', 'Mean', 'Max']  # 平整化列名
grouped = grouped.reset_index()  # 重置索引以便于绘图

# 绘图
fig, ax = plt.subplots(figsize=(10, 6))

# 设置柱状图的宽度
bar_width = 0.2
# 每组的x位置
x = range(len(grouped))

# 绘制柱状图
ax.bar([i - bar_width for i in x], grouped['Min'], bar_width, label='最小值', color='blue')
ax.bar(x, grouped['Mean'], bar_width, label='平均值', color='green')
ax.bar([i + bar_width for i in x], grouped['Max'], bar_width, label='最大值', color='red')

# 设置标签和标题
ax.set_xlabel('所属地区')
ax.set_ylabel('关注度')
ax.set_title('各所属地区的关注度')
ax.set_xticks(x)
ax.set_xticklabels(grouped['所属地区'], rotation=90)
ax.legend()

# 显示图形
plt.tight_layout()
plt.show()




