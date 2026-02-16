
import matplotlib.pyplot as plt
import numpy as np


#
#线型号  标记   颜色的代号
#
#颜色字符：'b' 蓝色，'m' 洋红色，'g' 绿色，'y' 黄色，'r' 红色，'k' 黑色，'w' 白色，'c' 青绿色，'#008000' RGB 颜色符串。
#多条曲线不指定颜色时，会自动选择不同颜色。
#线型参数：'‐' 实线，'‐‐' 破折线，'‐.' 点划线，':' 虚线。
#标记字符：'.' 点标记，',' 像素标记(极小点)，'o' 实心圈标记，'v' 倒三角标记，'^' 上三角标记，'>' 右三角标记，'<' 左三角标记...等等。
#如果我们要绘制坐标 (1, 3) 到 (8, 10) 的线，我们就需要传递两个数组 [1, 8] 和 [3, 10] 给 plot 函数：

#这是一个数据
figs = plt.figure()
xa = np.linspace(0,10,25)
ya = xa**2
yb = xa**3
yc = yb -500

axe0 = plt.axes()
axe0.plot(xa,ya,'ob')
plt.show()
"""
#绘制线条
plt.plot(xa,ya)
plt.show()
"""

"""
使用标记
#fmt '[marker][line][color]'
#跟随线后面的就是fmt参数
#ms 标记大小   mfc表示内部颜色   mec表示边框颜色
#marker
mar = np.array(['o','v'])
mar = 'v'
plt.plot(xa,ya,'b^-',xa,yb,'rv--',marker =mar,ms = 10)
plt.show()

"""


"""
#绘制多个曲线到一个图像上
plt.plot(xa,ya,'ro-')
plt.plot(xa,yb,'go-')
plt.plot(xa,yc,'bo-')
plt.show()
"""



