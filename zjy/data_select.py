# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 13:45:00 2020

@author: zjy
"""

from sklearn.datasets import load_iris
 
#导入IRIS数据集
iris = load_iris()
 
#特征矩阵
iris.data
 
#目标向量
iris.target
from sklearn.preprocessing import StandardScaler
 
#标准化，返回值为标准化后的数据
StandardScaler().fit_transform(iris.data)

from sklearn.preprocessing import MinMaxScaler
 
#区间缩放，返回值为缩放到[0, 1]区间的数据
MinMaxScaler().fit_transform(iris.data)
from sklearn.feature_selection import VarianceThreshold
 
#方差选择法，返回值为特征选择后的数据
#参数threshold为方差的阈值
VarianceThreshold(threshold=3).fit_transform(iris.data)

from sklearn.feature_selection import SelectKBest
from scipy.stats import pearsonr

#选择K个最好的特征，返回选择特征后的数据
#第一个参数为计算评估特征是否好的函数，该函数输入特征矩阵和目标向量，输出二元组（评分，P值）的数组，数组第i项为第i个特征的评分和P值。在此定义为计算相关系数
#参数k为选择的特征个数
SelectKBest(lambda X, Y: array(map(lambda x:pearsonr(x, Y), X.T)).T, k=2).fit_transform(iris.data, iris.target)

from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
 
#递归特征消除法，返回特征选择后的数据
#参数estimator为基模型
#参数n_features_to_select为选择的特征个数
RFE(estimator=LogisticRegression(), n_features_to_select=2).fit_transform(iris.data, iris.target)

#线性回归模型LassoCV，适用于参数较少的情况，传统的线性回归模型要求参数非线性相关，而LassoCV
#允许一定程度的线性相关，每次会删去一定量的参数。
#!/usr/bin/python
 
import pandas as pd
import numpy as np
import csv as csv
import matplotlib
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge, RidgeCV, ElasticNet, LassoCV, LassoLarsCV
from sklearn.model_selection import cross_val_score



train = pd.read_csv('train.csv', header=0)        # Load the train file into a dataframe
df = pd.get_dummies(train.iloc[:,1:-1])
df = df.fillna(df.mean())

X_train = df
y = train.price



def rmse_cv(model):
    rmse= np.sqrt(-cross_val_score(model, X_train, y, scoring="neg_mean_squared_error", cv = 3))
    return(rmse)

#调用LassoCV函数，并进行交叉验证，默认cv=3
model_lasso = LassoCV(alphas = [0.1,1,0.001, 0.0005]).fit(X_train, y)

#模型所选择的最优正则化参数alpha
print(model_lasso.alpha_)

#各特征列的参数值或者说权重参数，为0代表该特征被模型剔除了
print(model_lasso.coef_)

#输出看模型最终选择了几个特征向量，剔除了几个特征向量
coef = pd.Series(model_lasso.coef_, index = X_train.columns)
print("Lasso picked " + str(sum(coef != 0)) + " variables and eliminated the other " +  str(sum(coef == 0)) + " variables")

#输出所选择的最优正则化参数情况下的残差平均值，因为是3折，所以看平均值
print(rmse_cv(model_lasso).mean())


#画出特征变量的重要程度，这里面选出前3个重要，后3个不重要的举例
imp_coef = pd.concat([coef.sort_values().head(3),
                     coef.sort_values().tail(3)])

matplotlib.rcParams['figure.figsize'] = (8.0, 10.0)
imp_coef.plot(kind = "barh")
plt.title("Coefficients in the Lasso Model")
plt.show() 