import numpy
import pandas as pd

df = pd.read_csv('', header = None)

flow_relation = df.drop(['state', 'point'], axis=1)
flow_relation.to_json('flow_relation.json', orient="values",force_ascii=False)

flow_weight = df.drop(['state', 'point'], axis=1)
flow_weight.to_json('flow_weight.json', orient="values",force_ascii=False)
