import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
#列表生成1-9的 变量 标签
indexes = [str(a+1) +"号" for a in np.linspace(0,8,9)]
indexes = np.array(indexes)

#使用concanate纵向拼接九个数组
#c = np.random.normal(5,2,(12,9))
c = np.random.normal(5,2,(1,9))
for a in range(2,13):
    c = np.concatenate((c,  7*np.random.normal(a,1,(1,9))),axis=0)

data = pd.DataFrame(c,columns=indexes)
os.chdir("D:/hl")
data.to_csv("basic_data.csv")
#(12,9) is shape
print(data.values[11,:])

sns.set(style ="whitegrid")
for a in range(0,9):
    x = np.random.rand(12)*a 
    y = data.values[:,a]
    
    plt.scatter(x,y,c=(y/x),cmap = 'hot',marker = '+')




    #球x与x**2的相关系数

x = np.random.randn(20)
ys = x**2
print("相关系数",np.corrcoef(x,ys))


plt.colorbar()
plt.show()

#生成12个 9特征值，值为对应行标的正太分布数据