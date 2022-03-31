import pandas as pd
import csv
import numpy

a = pd.read_csv("graph_example.csv")
d = {'vertex': [0] * 100000, 'target': [0] * 100000, 'weight': [0] * 100000}
for i in range(100000):
    d['vertex'][i] = i
for i in range(len(a['weight'])):
    d['weight'][a['v1'][i]] += int(a['weight'][i])
    d['weight'][a['v2'][i]] += int(a['weight'][i])
b = pd.read_csv("target.csv")
for i in range(len(b['vertex'])):
    d['target'][i] = b['target'][i]
d1 = pd.DataFrame(d)
d1.to_excel('Tables/2.xlsx', index=False)
