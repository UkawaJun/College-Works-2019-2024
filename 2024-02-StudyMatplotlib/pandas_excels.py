import numpy as np
import pandas as pd

df = pd.read_csv('data.csv',index_col = 0)

arr = df.values
print(df)
print('\n')
print(df.keys)
print('\n')
print(df.values)
print(df.iloc[0:6,0:6])


print("补充填充值,dropna以及搜捕矩阵")
hl = df.iloc[:,1]
df = df.fillna("pawa")
choice = df == "pawa"
print(choice)
ndf = df[choice].dropna(how = 'all')
print(ndf.T.dropna(how = 'all').T)
print()
l = ndf.T.dropna(how = 'all').T
lchoice = l == 'pawa'
l[lchoice] = 50
l = l.fillna(0)
print(l,'--------------------------\n')
df.iloc[0:3,1:3] = 5

print(df)