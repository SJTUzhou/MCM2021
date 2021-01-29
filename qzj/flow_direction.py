import numpy
import pandas as pd

df = pd.read_csv('zjy/task_one.csv', header = None)

df = pd.concat([df, df[0].str.split('_', expand=True)], axis=1,names='PORT_END')

flow_relation = df.drop([2], axis=1)
flow_relation = flow_relation.drop([3], axis=1)
flow_relation.to_json('qzj/flow_relation.json', orient="values",force_ascii=False)

flow_weight = df.drop([2], axis=1)
flow_weight.to_json('qzj/flow_weight.json', orient="values",force_ascii=False)
