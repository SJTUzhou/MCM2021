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
