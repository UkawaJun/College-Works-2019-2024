import math
from tkinter import Label
import matplotlib.pyplot as plt
import numpy as np

# 正确显示正负号
plt.rcParams['axes.unicode_minus'] = False

# 生成正弦曲线
x = np.array([2,4,6,8,10])
y = np.array([80,82,85,90,92])
y_error = 4*np.array([1,2,1,2,1])


# 设置图形框架
fig = plt.figure()
axis = fig.add_subplot(111)

plt.grid(axis = 'y')
plt.bar(x,y,width = 1,color = 'k',label = 'tem')
plt.errorbar(x, y, yerr=y_error, fmt='o')
plt.xlabel("Time")
plt.ylabel("Tempture")
plt.title("Tempture / Time")

#plt.legend(loc='best')
plt.show()