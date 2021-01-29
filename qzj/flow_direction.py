import numpy
import pandas as pd

df = pd.read_csv('zjy/task_one.csv', header = None)
df = df.drop(df.index[0])
df = df.drop([2], axis=1)
df = pd.concat([df, df[0].str.split('_', expand=True)], axis=1)
df.columns = [0,1,2,3]
df = df.drop([0], axis=1)

order = [2, 3, 1]
df = df[order]

flow_relation = df.drop([1], axis=1)
flow_relation.to_json('qzj/flow_relation.json', orient="values",force_ascii=False)

df[1] = pd.to_numeric(df[1])
df.to_json('qzj/flow_weight.json', orient="values",force_ascii=False)
