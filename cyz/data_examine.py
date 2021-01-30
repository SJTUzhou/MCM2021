import pandas as pd
myDataDir = "H:/Data for Problem C_MCM 2021/"
file2 = "2. Transaction order_ordinary goods .csv"
df2 = pd.read_csv(myDataDir+file2,sep=',')
# print(df2.head())
temp1 = df2.loc[(df2['PORT_BEGIN'] == "宁波") & (df2['PORT_END'] == "新港")]
print(temp1)
# print(temp1["AMT"])
print(pd.unique(temp1["AMT"]))
print(pd.unique(temp1["CGO_BRIEF_DESC_NME"]))
# print(pd.unique(temp1["WBL_AUD_DT"]))
