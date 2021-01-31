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


# 是否考虑集装箱体积
df2["VOLUME"] = 1
# df2["VOLUME"] = df2["CNTR_TYPE"]

myDirTsk2_3 = "营口_宁波"#'上海_烟台' 
temp_df = df2.loc[(df2["DIRECTION"]==myDirTsk2_3) & (df2["IS_EMPTY"]==0)]
temp_df = temp_df[["SVVD","WBL_AUD_DT","AMT","VOLUME"]]

# 计算每日每个SVVD发货量和每个SVVD每日总运费
statistic_df = temp_df.groupby(["SVVD","WBL_AUD_DT"])[['AMT',"VOLUME"]].sum().reset_index()
# 时间日期->距离航行前天数
statistic_df["WBL_AUD_DT"] = statistic_df.groupby(["SVVD"])["WBL_AUD_DT"].transform(lambda x: x.max()-x)
statistic_df["WBL_AUD_DT"] = statistic_df["WBL_AUD_DT"].apply(lambda x: x.days)

# 这个Direction的SVVD总数量
num_SVVD = pd.unique(statistic_df["SVVD"]).shape[0]
avgSVVD_Vol = statistic_df["VOLUME"].sum()/num_SVVD
print("the avg volume per SVVD of this direction {}".format(avgSVVD_Vol))
print("the total volume of this direction {}".format(statistic_df["VOLUME"].sum()))




dailyVol_df = statistic_df.groupby(["WBL_AUD_DT"])[['AMT',"VOLUME"]].sum().reset_index()
# 计算平均每日1个SVVD发货量和平均每日1个SVVD总运费
dailyVol_df['AMT'] = dailyVol_df['AMT']/num_SVVD
dailyVol_df['VOLUME'] = dailyVol_df['VOLUME']/num_SVVD
print(dailyVol_df["VOLUME"].sum())


plt.scatter(dailyVol_df["WBL_AUD_DT"], dailyVol_df["VOLUME"], marker="^", s=8)
plt.ylabel("Daily Sales Volume")
plt.xlabel("Date")
plt.show()


# svvd_dfs = []
# all_svvd_df = pd.DataFrame(columns=statistic_df.columns)
# for svvd in pd.unique(statistic_df["SVVD"]):
#     part_df = statistic_df.loc[statistic_df["SVVD"]==svvd]
#     svvd_dfs.append(part_df)
#     all_svvd_df = all_svvd_df.append(part_df)

# print(svvd_dfs[0:3])
# fig, axs = plt.subplots(1, len(svvd_dfs))
# for i in range(len(svvd_dfs)):
#     axs[i].scatter(svvd_dfs[i]["WBL_AUD_DT"], svvd_dfs[i]["VOLUME"], marker="o", s=8)
#     axs[i].scatter(dailyVol_df["WBL_AUD_DT"], dailyVol_df["VOLUME"], marker="^", s=8)
#     axs[i].set_ylabel("Daily Volume")
#     axs[i].set_xlabel("Date")
# plt.show()


# all_svvd_df.rename(columns={'WBL_AUD_DT':'BEFORE_DAYS'}, inplace=True)
# all_svvd_df.to_csv("./task2_3_{}.csv".format(myDirTsk2_3), index=False)