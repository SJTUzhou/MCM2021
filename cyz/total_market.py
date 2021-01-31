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
df2["CNT"] = 1

# 修改container容积
df2["CNTR_TYPE"] = df2["CNTR_TYPE"].apply(lambda x: int(x[:2]))

statistic_df = df2.groupby(["WBL_AUD_DT"])[["CNTR_TYPE","AMT","CNT"]].sum().reset_index()
statistic_df["WBL_AUD_DT"] = statistic_df["WBL_AUD_DT"].transform(lambda x: x-x.min())
statistic_df["WBL_AUD_DT"] = statistic_df["WBL_AUD_DT"].apply(lambda x: x.days)

figs, axs = plt.subplots(1,2)
# 所有direction每日总volume和每日平均价格
axs[0].scatter(statistic_df["WBL_AUD_DT"], statistic_df["CNTR_TYPE"], marker="^")
axs[1].scatter(statistic_df["WBL_AUD_DT"], statistic_df["AMT"]/statistic_df["CNT"], marker="o")
plt.show()