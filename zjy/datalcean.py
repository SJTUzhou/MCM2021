import numpy
import pandas as pd

test_df = pd.read_csv(r'1. Transaction order_container.csv', header = None)
test_df[test_df.isnull().values==True]
test_df=test_df.dropna(axis=0,subset=[7])

test_df.to_csv("1_gai_Transaction order_container.csv.csv",index=False,sep=',')

dataf3=pd.read_excel('3. Contain route.xlsx',sheet_name='2.xlsx')
dataf3[dataf3.isnull().values==True]
dataf3=dataf3.dropna(axis=0,subset=[0,1])

dataf4=pd.read_excel('4. Labels of C-S.xlsx')
dataf4[dataf4.isnull().values==True]
dataf4=dataf4.dropna(axis=0)
dataf4.to_csv("4_gai_Labels of C-S.xlsx.csv",index=False,sep=',')

dataf5=pd.read_csv(r'5. Container information.csv', header = None)
dataf5[dataf4.isnull().values==True]

dataf6=pd.read_excel('6. Existing pricing strategy.xlsx')
dataf6[dataf6.isnull().values==True]