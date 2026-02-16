

from matplotlib import figure
import matplotlib.pyplot as plt
import numpy as np


xa = np.linspace(-20,20,50)
xb = xa**2
yb = (xa**2)/3
sizes = xb/5

xa2 = np.random.rand(50)
ya2 = np.random.rand(50)
"""
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([1, 4, 9, 16, 7, 11, 23, 18])
colors = 
np.array(["red","green","black","orange","purple","beige","cyan","magenta"])
#可以逐点定义颜色
"""

"""
plt.scatter(xa, xb, s=sizes,color = 'orange')
plt.scatter(xa, yb, s=sizes/2)
plt.show()

"""

"""
colors = np.random.rand(50)
alphas = np.random.rand(50)
area = (30 * np.random.rand(50))**2  # 0 to 15 point radii

plt.scatter(xa2, ya2, s=area, c=colors, alpha=alphas) # 设置颜色及透明度


plt.show()

"""


###################colorMap####################
#说白了就是可以显示一个颜色条 --- 如热力图
plt.figure()
colors = np.linspace(0,100,50)

plt.scatter(xa2, ya2, c=colors, cmap='viridis')

plt.colorbar()
plt.show()

