import csv
import pandas as pd
import numpy as np

path=r'direction.csv'

with open(path,encoding = 'utf-8') as f:
    data = np.loadtxt(f,delimiter = ",",skiprows = 1,usecols = (1,2,3,4,5,6,7)) #跳过第一行，跳过第一列


gen=np.sqrt(np.sum(np.square(data), axis=0)) #每一列平方和开根号

for i in range(7):
    data[:,i]=data[:,i]/gen[i]

arv_min=data.min(axis=0)

arv_max=data.max(axis=0)

for i in range(7):
    data[:,i]=(data[:,i]-arv_min[i])/(arv_max[i]-arv_min[i])

w=[0,0.5454,0.3045,0,0,0.0486,0.1015]#权重向量

score = np.zeros((data.shape[0], 1))
score[:,0]=data[:,0]*w[0]+data[:,1]*w[1]+data[:,2]*w[2]+data[:,3]*w[3]+data[:,4]*w[4]+data[:,5]*w[5]+data[:,6]*w[6]


df1 = pd.read_csv(path,sep=',')

df1['score']=pd.DataFrame(score)
df2 = df1.sort_values(by='score', ascending=False)
df2.to_csv("TOPSIS.csv", index=False)