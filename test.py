from datetime import datetime
import pandas as pd

transactions_df = pd.read_csv("transactions.csv")
str = transactions_df['to HKD'][0]
str = str.replace('[','')
str = str.replace(']','')
a = str.split(', ')
for i in range(len(a)):
    a[i] = float(a[i])
print(a)
print(type(a))
print(sum(a))

#print(type(tuple(currencies_dict.keys())))