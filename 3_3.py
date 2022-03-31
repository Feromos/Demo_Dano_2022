import pandas as pd
import csv
import numpy

a = pd.read_csv("task3_data.csv")
d1 = {}
for i in range(len(a['party_rk'])):
    if a['russian_region_nm'][i] not in d1:
        d1[a['russian_region_nm'][i]] = [9999999999, 0]
    d1[a['russian_region_nm'][i]][0] = min(a['purchase_sum'][i], d1[a['russian_region_nm'][i]][0])
    d1[a['russian_region_nm'][i]][1] = max(a['purchase_sum'][i], d1[a['russian_region_nm'][i]][1])
d3 = {'region': [], 'value': []}
for i in d1:
    d3['region'].append(i)
    d3['value'].append(d1[i][1] - d1[i][0])
d1_1 = pd.DataFrame(d3)
d1_1.to_excel('Tables/3_inequality.xlsx', index=False)
