import pandas as pd
import csv
import numpy

a = pd.read_csv("task3_data.csv")
d1 = {}
d2 = {}
for i in range(len(a['party_rk'])):
    if a['russian_region_nm'][i] not in d1:
        d1[a['russian_region_nm'][i]] = [0, 0, '']
    d1[a['russian_region_nm'][i]][0] += a['purchase_sum'][i]
    d1[a['russian_region_nm'][i]][1] += 1
    d1[a['russian_region_nm'][i]][2] = a['timediff_to_msk_hour_cnt'][i]
    if a['russian_federal_district_cd'][i] > 0:
        if a['russian_federal_district_cd'][i] not in d2:
            d2[a['russian_federal_district_cd'][i]] = [0, 0]
        d2[a['russian_federal_district_cd'][i]][0] += a['purchase_sum'][i]
        d2[a['russian_federal_district_cd'][i]][1] += 1
d3 = {'region': [], 'value': [], 'time': []}
d4 = {'district': [], 'value': []}
for i in d1:
    d3['region'].append(i)
    d3['value'].append(d1[i][0] / d1[i][1])
    d3['time'].append(d1[i][2])
for i in d2:
    d4['district'].append(i)
    d4['value'].append(d2[i][0] / d2[i][1])
d1_1 = pd.DataFrame(d3)
d1_1.to_excel('Tables/3_region.xlsx', index=False)
d2_1 = pd.DataFrame(d4)
d2_1.to_excel('Tables/3_district.xlsx', index=False)
