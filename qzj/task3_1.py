import pandas as pd
import numpy as np

#import matplotlib.pyplot as plt


df = pd.read_csv('zjy/task2_1.csv')

def calculate_daily_volume(freight_rate_per_volume):
    # parameter a, b are determined by function fitting of matlab
    a = 1768
    b = -0.1853
    freight_rate_per_volume = np.array(freight_rate_per_volume)
    daily_volume = a * np.exp(b * freight_rate_per_volume)
    return daily_volume

# 左闭右开，输出当前区间的总income
def cal_money(df, rate_list, start_day, end_day, rate_gate, discount):
    date_list = df['date_before_sailing'].values
    df = df.set_index('date_before_sailing', drop=True)
    start_day_list = 14 - date_list
    #day = start_day_list[0]
    new_AMT = 0
    old_AMT = 0
    count = 0
    unchanged = True
    for day in start_day_list:
        day_index = 14 - day
        
        if (((discount > 1) and (rate_list[count] > rate_gate)) or ((discount < 1) and (rate_list[count] < rate_gate)) and unchanged):
            print('涨或降价')
            unchanged = False
            old_AMT_tmp = df.loc[day_index,'AMT']
            old_AMT = old_AMT + old_AMT_tmp
            if day >= start_day & day < end_day:   
                today_price = df.loc[day_index,'AMT']
                sales = df.loc[day_index,'sales_count_per_SVVD'] # 销量
                today_price = today_price/sales # 单价
                new_price = today_price + abs(today_price)*(discount-1) # 新单价，后面可以修改影响后的销量
                new_sales = df.loc[day_index,'sales_count_per_SVVD'] # 新销量
                #new_sales = calculate_daily_volume(new_price/40)
                new_AMT_tmp = new_price*new_sales
                new_AMT = new_AMT + new_AMT_tmp
                print('in the day range')
                
            else:
                print('out of day range')

        else:
            new_AMT_tmp = df.loc[day_index,'AMT']
            new_AMT = new_AMT + new_AMT_tmp
            print('平价')
        
        count = count + 1
    return(new_AMT, old_AMT)


# 提取日期
df['WBL_AUD_DT'] = pd.to_datetime(df['WBL_AUD_DT'].str.replace(' ', '  ').str[0:10].str.strip(), format = '%Y/%m/%d')

SVVD_list = pd.unique(df['SVVD'])
svvd_df = df['SVVD']
#df[df['DIRECTION'] == '钦州_宁波' & df['SVVD'] == '0']

df.dropna(axis=0, how='any', inplace=True)
temp_df = df.loc[(df["DIRECTION"]=='钦州_宁波')]
temp_df = temp_df[["SVVD","WBL_AUD_DT","AMT"]]
statistic_df = temp_df.groupby(["SVVD","WBL_AUD_DT"])[['AMT']].sum().reset_index()
# print(1)

# 距离离港有几天
statistic_df['WBL_AUD_DT'].astype('datetime64[D]')
#tmp_1_df = statistic_df.groupby(['SVVD'])
SVVD_list = pd.unique(statistic_df['SVVD'])

tmp3 = temp_df['SVVD'].value_counts(ascending=True).to_frame()
tmp3.rename({'SVVD': 'sales_count'}, axis=1, inplace=True)

daily_sales = temp_df[["SVVD", "WBL_AUD_DT"]].value_counts()
daily_sales = daily_sales.reset_index().sort_values(by=['SVVD', 'WBL_AUD_DT'], ascending=[True, True])
daily_sales.rename({0:'sales_count_per_day'}, axis=1, inplace=True)
daily_sales = daily_sales.reset_index()
statistic_df = pd.concat([statistic_df, daily_sales['sales_count_per_day']], axis=1)

global tmp
tmp=pd.DataFrame()
new_income_list = []
old_income_list = []
for svvd in SVVD_list:
    same_svvd = statistic_df.loc[statistic_df['SVVD'] == svvd]
    time_list = pd.unique(same_svvd['WBL_AUD_DT'])
    time_before = time_list[-1] - time_list
    time_before_days = time_before.astype('timedelta64[D]').astype(int)
    svvd_info = pd.concat([same_svvd,pd.DataFrame(time_before_days, index=same_svvd.index)], axis=1)
    a = tmp3.loc[svvd].values
    svvd_info['sales_count_per_SVVD'] = a[0]
    svvd_info.rename({0: 'date_before_sailing'}, axis=1, inplace=True)
    #sold_rate
    #svvd_info.reset_index()
    first_index = svvd_info.index.values
    sold_total = svvd_info['sales_count_per_day'].loc[first_index[0]]
    rate_list = []
    rate_list.append(sold_total/a[0])
    for i in range(first_index[0]+1, first_index[0]+len(svvd_info)):
        sold_i = svvd_info['sales_count_per_day'].loc[i]
        sold_total = sold_total + sold_i
        rate_i = sold_total/a[0]
        rate_list.append(rate_i)
    new_income1, old_income1 = cal_money(svvd_info, rate_list, 0, 5, 0.5, 1.3)
    new_income2, old_income2 = cal_money(svvd_info, rate_list, 5, 7, 0.3, 0.5)
    new_income3, old_income3 = cal_money(svvd_info, rate_list, 5, 7, 0.6, 1.4)
    new_income4, old_income4 = cal_money(svvd_info, rate_list, 7, 8, 0.7, 1.4)
    new_income5, old_income5 = cal_money(svvd_info, rate_list, 8, 15, 0.4, 0.5)
    new_income6, old_income6 = cal_money(svvd_info, rate_list, 8, 15, 0.9, 1.2)
    new_income7, old_income7 = cal_money(svvd_info, rate_list, 8, 15, 0.8, 1.2)

    new_income = new_income1 + new_income2 + new_income3 + new_income4 + new_income5 + new_income6 + new_income7
    old_income = old_income1 + old_income2 + old_income3 + old_income4 + old_income5 + old_income6 + old_income7
    new_income_list.append(new_income)
    old_income_list.append(old_income)
    b = pd.DataFrame(rate_list)
    b.set_index(pd.Series(range(first_index[0], first_index[0]+len(svvd_info))))
    b.rename({0: 'sold_rate'}, axis=1, inplace=True)
    #tmp = pd.concat([svvd_info, b], axis=1)
    tmp = pd.concat([tmp, svvd_info])
    
    tmp = tmp.sort_values(by=['SVVD', 'WBL_AUD_DT'], ascending=[False, False])
    print(2)
    
    
imcome_change = pd.DataFrame({'SVVD': SVVD_list, 'new_income': new_income_list, 'old_income': old_income_list})

#tmp_2 = tmp.sort_values(by='SVVD', ascending=True)
#tmp_2.to_csv('qzj/habbits/sales_counts_AMT.csv')
#time_list_df = pd.unique(statistic_df.groupby(['SVVD'])[['WBL_AUD_DT']])
##statistic_df['date_before_sailing']=.apply(lambda x : x[-1:] -x[0:])

# 注意里面的AMT是当天累计的售价和，单价要除以'sales_count_per_day'
#tmp = pd.concat([tmp, daily_sales['sales_count_per_day']], axis=1)

#tmp_2['sales_count']
print(1)

# 利用率