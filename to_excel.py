import pandas as pd
import csv
import numpy

a = pd.read_csv("graph_example.csv")
a.to_excel('graph_example.xlsx', index=False)
