import pandas as pd
myDataDir = "H:/Data for Problem C_MCM 2021/"
file1 = "1. Transaction order_container.csv"
df1 = pd.read_csv(myDataDir+file1,sep=',')

df1["DIRECTION"] = df1['PORT_BEGIN'] + df1['PORT_END']
direction_list = pd.unique(df1["DIRECTION"])

info_dict = {}

# 示例前10个
for direction in direction_list[:10]:
    temp_dataframe = df1.loc[df1["DIRECTION"]==direction]
    freight_rates = temp_dataframe["AMT"]
    revenue = freight_rates.sum()
    info_dict[direction] = {"revenue":revenue}

print(info_dict)
