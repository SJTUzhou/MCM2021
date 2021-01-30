import numpy
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('zjy/TOPSIS.csv', index_col=False,)
df = pd.concat([df,df['DIRECTION'].str.split('_', expand=True)], axis=1)

df.rename({0: 'BEGIN', 1:'END'}, axis=1, inplace=True)

G = nx.DiGraph()
begin_list = df['BEGIN'].astype(str)
end_list = df['END'].astype(str)
weight_list = df['score'].astype(float)
for i in range(len(begin_list)):
    G.add_edge(begin_list[i], end_list[i], weight=weight_list[i])

#nx.draw(G, nx.random_layout(G))
#plt.show()

df1 = df['BEGIN']
df2 = df['END']

flow_relation = pd.concat([df1,df2],axis=1)
#flow_relation.to_json('qzj/flow_relation.json', orient="values",force_ascii=False)

a = flow_relation[0:1000].to_dict('records')
f = open("qzj/d3-Sticky-Force-Layout-master/1.js", "w")
f.write(str(a))
f.close()

#df[5] = pd.to_numeric(df[5])
#flow_weight = df.groupby([[9,10,5]]).sum()
#flow_weight.to_json('qzj/flow_weight.json', orient="values",force_ascii=False)
