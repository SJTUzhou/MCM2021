import pandas as pd
import matplotlib.pyplot as plt
myDataDir = "H:/Data for Problem C_MCM 2021/"
file2 = "2. Transaction order_ordinary goods .csv"



df2 = pd.read_csv(myDataDir+file2,sep=',')
# 删除缺失值
df2.dropna(axis=0, how='any', inplace=True)

df2["DIRECTION"] = df2['PORT_BEGIN'] + "_" + df2['PORT_END']
# 修改时间，保留年月日
df2["WBL_AUD_DT"] = df2["WBL_AUD_DT"].apply(lambda x: pd.to_datetime(x.split()[0]))


# 修改container容积
df2["CNTR_TYPE"] = df2["CNTR_TYPE"].apply(lambda x: int(x[:2]))

'''

dir_dfs = []

top10_dirs = ['新港_南沙','营口_南沙','营口_宁波','钦州_宁波','营口_福清','营口_钦州','上海_烟台','日照_铁山','上海_武汉','乐从_营口']
for direction in top10_dirs:
    temp_df = df2.loc[(df2["DIRECTION"]==direction) & (df2["IS_EMPTY"]==0)]
    if temp_df.empty:
        continue
    dir_dfs.append(temp_df[["SVVD","WBL_AUD_DT","AMT","CNTR_TYPE","DIRECTION"]])


# 列表存储8个direction的名称，SVVD，DATE，AMT_SUM
df_DIR_SVVD_DATE_AMT_lst = []
for dir_df in dir_dfs:
    df_DIR_SVVD_DATE_AMT = dir_df.groupby(["DIRECTION","SVVD","WBL_AUD_DT"])[['AMT',"CNTR_TYPE"]].sum().reset_index()
    df_DIR_SVVD_DATE_AMT_lst.append(df_DIR_SVVD_DATE_AMT)

print(df_DIR_SVVD_DATE_AMT_lst[0])
'''
# 是否考虑集装箱体积
df2["CNT"] = 1
df2["VOLUME"] = df2["CNTR_TYPE"] # 或等于1意味着不考虑单位容积

myDirTsk3_1 = '钦州_宁波'#'营口_宁波'# 
temp_df = df2.loc[(df2["DIRECTION"]==myDirTsk3_1) & (df2["IS_EMPTY"]==0)]
temp_df = temp_df[["SVVD","WBL_AUD_DT","AMT","VOLUME","DIRECTION","CNT"]]
print(temp_df)

# 计算每日平均发货量和每日平均运费
statistic_df = temp_df.groupby(["DIRECTION","SVVD","WBL_AUD_DT"])[['AMT',"VOLUME","CNT"]].sum().reset_index()

# Each direction, each SVVD, each day: avg freight rate and daily volume
statistic_df["AMT"] = statistic_df["AMT"]/statistic_df["VOLUME"] # statistic_df["CNT"]
# print(statistic_df)
plt.scatter(statistic_df["AMT"],statistic_df["VOLUME"], marker="^")
plt.ylabel("Daily sales volume")
plt.xlabel("Average freight rate per unit of volume")
plt.show()
# statistic_df.to_csv("./{}.csv".format(myDirTsk3_1), index=False)



'''
num_SVVD = pd.unique(statistic_df["SVVD"]).shape[0]
avgSVVD_Vol = statistic_df["VOLUME"].sum()/num_SVVD
print("the avg volume per SVVD of this direction {}".format(avgSVVD_Vol))
print("the total volume of this direction {}".format(statistic_df["VOLUME"].sum()))
# 生成每日平均发货量随时间变化图

statistic_df["WBL_AUD_DT"] = statistic_df.groupby(["SVVD"])["WBL_AUD_DT"].transform(lambda x: x.max()-x)
statistic_df["WBL_AUD_DT"] = statistic_df["WBL_AUD_DT"].apply(lambda x: x.days)

dailyVol_df = statistic_df.groupby(["DIRECTION","WBL_AUD_DT"])[['AMT',"VOLUME"]].sum().reset_index()

dailyVol_df['AMT'] = dailyVol_df['AMT']/num_SVVD
dailyVol_df['VOLUME'] = dailyVol_df['VOLUME']/num_SVVD
print(dailyVol_df["VOLUME"].sum())
plt.scatter(dailyVol_df["WBL_AUD_DT"], dailyVol_df["VOLUME"], marker="^")
plt.ylabel("Daily Volume")
plt.xlabel("Date")
plt.show()
'''