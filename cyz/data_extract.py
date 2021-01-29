import pandas as pd
import numpy as np
myDataDir = "H:/Data for Problem C_MCM 2021/"
file1 = "1. Transaction order_container.csv"
df1 = pd.read_csv(myDataDir+file1,sep=',')

# 删除缺失值
df1.dropna(axis=0, how='any', inplace=True)


df1["DIRECTION"] = df1['PORT_BEGIN'] + df1['PORT_END']
direction_list = pd.unique(df1["DIRECTION"])

info_list = []

for direction in direction_list:
    temp_dataframe = df1.loc[df1["DIRECTION"]==direction]
    freight_rates = temp_dataframe["AMT"]
    container_volumes = pd.Series([int(element[:2]) for element in temp_dataframe["CNTR_TYPE"]])
    revenue = int(freight_rates.sum())
    volume = container_volumes.sum()
    volume_counts = container_volumes.value_counts()
    num_20 = 0
    num_40 = 0
    if 20 in volume_counts.keys():
        num_20 = volume_counts[20]
    if 40 in volume_counts.keys():
        num_40 = volume_counts[40]
    freight_rate = freight_rates.mean()
    myDict = {"DIRECTION": direction, "REVENUE":revenue, "SALES_VOLUME":volume, "FREIGHT_RATE":freight_rate, "NUM_40":num_40, "NUM_20":num_20}
    info_list.append(myDict) 

info_df = pd.DataFrame(info_list)
info_df.to_csv("./direction.csv", index=False)

