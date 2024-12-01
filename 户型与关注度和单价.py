import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 配置字体
config = {
    "font.family": 'serif',
    "mathtext.fontset": 'stix',
    "font.serif": ['SimSun'],  # 宋体
    'axes.unicode_minus': False  # 处理负号
}
rcParams.update(config)


df = pd.read_excel("二手房.xlsx")
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

### 第一个图 - 折线图 (户型与平均单价的关系)
mean_by_type_price = df.groupby('户型')['单价'].mean()
axes[0].plot(mean_by_type_price.index, mean_by_type_price.values, marker='o', linestyle='--', color='b')
axes[0].set_title('户型与平均单价的关系', fontsize=16)
axes[0].set_xlabel('户型', fontsize=12)
axes[0].set_ylabel('平均单价 (元/平方米)', fontsize=12)
for x, y in zip(mean_by_type_price.index, mean_by_type_price.values):
    axes[0].annotate(f'{y:.0f}', xy=(x, y), xytext=(0, 5), textcoords='offset points', ha='center', fontsize=15, color='black')
axes[0].grid(True)
axes[0].tick_params(axis='x', rotation=45)

### 第二个图 - 柱状图 (不同户型的平均关注度)
mean_by_type_attention = df.groupby('户型')['关注度'].mean()
axes[1].bar(mean_by_type_attention.index, mean_by_type_attention.values, width=0.5, alpha=0.6, color='red')
axes[1].set_title('不同户型的平均关注度', fontsize=16)
axes[1].set_xlabel('户型', fontsize=12)
axes[1].set_ylabel('平均关注度', fontsize=12)
for x, y in zip(mean_by_type_attention.index, mean_by_type_attention.values):
    axes[1].text(x, y + 5, f'{y:.0f}', ha='center', va='bottom', fontsize=20, color='black')

axes[1].tick_params(axis='x', rotation=30)
plt.tight_layout()
plt.show()

