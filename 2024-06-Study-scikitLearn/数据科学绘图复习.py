from cProfile import label
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

print(os.getcwd())
"""
x=['a','b','c']
y1 =[1,5,8]
y2 = [10,15,16]

plt.bar(x,y1,label = 'y1')
plt.bar(x,y2,label = 'y2')
"""

x_value = [np.random.randint(140,180,i) for i in [100,200,300]]
print(x_value)
 

plt.hist(x_value,bins=10,edgecolor="r",histtype="bar",alpha=0.5,label=["A公司","B公司","C公司"])

plt.show()

