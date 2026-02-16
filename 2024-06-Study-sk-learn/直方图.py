from cProfile import label
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

x1 = np.linspace(0,50,3)
y1 = np.linspace(0,550,3)
y2 = np.linspace(0,520,3)

labels =['1','2','3']

plt.bar(labels,y1,label = '2016')
plt.bar(labels,y2,label = '2017')

plt.xticks(np.arange(5)+0.2, labels)
plt.show()

