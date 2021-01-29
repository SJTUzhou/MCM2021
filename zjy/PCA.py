import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
plt.rc('font', **{'family': 'Microsoft YaHei, SimHei'})
# 设置中文字体的支持

df = pd.read_csv('loan_apply.csv')
df = pd.DataFrame(file)
print(df)
# 求解相关系数矩阵，证明做主成分分析的必要性
## 丢弃无用的 ID 列
data = df.drop(columns='ID')

import seaborn as sns
sns.heatmap(data.corr(), annot=True)
# annot=True: 显示相关系数矩阵的具体数值

# PCA 通常用中心标准化，也就是都转化成 Z 分数的形式
from sklearn.preprocessing import scale
data = scale(data)
from sklearn.decomposition import PCA
pca = PCA(n_components=5) # 直接与变量个数相同的主成分
pca.fit(data)