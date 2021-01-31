import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('zjy/task2_1.csv')

# 提取日期
df['WBL_AUD_DT'] = pd.to_datetime(df['WBL_AUD_DT'].str.replace(' ', '  ').str[0:10].str.strip(), format = '%Y/%m/%d')

SVVD_list = pd.unique(df['SVVD'])
svvd_df = df['SVVD']
#df[df['DIRECTION'] == '钦州_宁波' & df['SVVD'] == '0']

df.dropna(axis=0, how='any', inplace=True)
temp_df = df.loc[(df["DIRECTION"]=='钦州_宁波')]
temp_df = temp_df[["SVVD","WBL_AUD_DT","AMT"]]
statistic_df = temp_df.groupby(["SVVD","WBL_AUD_DT"])[['AMT']].sum().reset_index()
print(1)

# 距离离港有几天
statistic_df['WBL_AUD_DT'].astype('datetime64[D]')
#tmp_1_df = statistic_df.groupby(['SVVD'])
SVVD_list = pd.unique(statistic_df['SVVD'])

tmp3 = temp_df['SVVD'].value_counts(ascending=True).to_frame()
tmp3.rename({'SVVD': 'sales_count'}, axis=1, inplace=True)

global tmp
tmp=pd.DataFrame()
for svvd in SVVD_list:
    same_svvd = statistic_df.loc[statistic_df['SVVD'] == svvd]
    time_list = pd.unique(same_svvd['WBL_AUD_DT'])
    time_before = time_list[-1] - time_list
    time_before_days = time_before.astype('timedelta64[D]').astype(int)
    svvd_info = pd.concat([same_svvd,pd.DataFrame(time_before_days, index=same_svvd.index)], axis=1)
    a = tmp3.loc[svvd].values
    svvd_info['sales_count'] = a[0]
    tmp = pd.concat([tmp, svvd_info])
    
    

tmp.rename({0: 'date_before_sailing'}, axis=1, inplace=True)
tmp_2 = tmp.sort_values(by='SVVD', ascending=True)
tmp_2.to_csv('qzj/habbits/sales_counts_AMT.csv')
#time_list_df = pd.unique(statistic_df.groupby(['SVVD'])[['WBL_AUD_DT']])
##statistic_df['date_before_sailing']=.apply(lambda x : x[-1:] -x[0:])

#tmp_2['sales_count']
#print(1)