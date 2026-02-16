from pickle import MARK
import matplotlib.pyplot as plt
import numpy as np

#符号函数  结合map函数使用
def signs(num):
    signs = [-1]
    if num % 3 ==0:
        signs[0] = 1
    return signs[0]

#先用numpy做一点绘图数据
funx = lambda a : a> 50
funx2 = lambda a : list(map(signs,a))

xa = np.arange(0,110,2)
xb = funx2(xa) +xa

#轴标题
plt.title("RUNOOB TEST TITLE")
plt.xlabel("x - label")
plt.ylabel("y - label")

#轴线
plt.grid(axis = 'x',color = 'r', linestyle = '--', linewidth = 1.0)

plt.plot(xa,xb)
plt.show()
