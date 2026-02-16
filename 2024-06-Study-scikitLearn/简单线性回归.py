import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

w = pd.read_csv("cars.csv")
x = np.array(w['speed']).reshape(-1,1)
y = np.array(w['dist']).reshape(-1,1)

from sklearn import  linear_model
reg = linear_model.LinearRegression()
reg.fit(x,y)
print(reg.coef_,reg.intercept_)

plt.figure(figsize = (10,4.5))
#plt.plot(x,y,'s',label = 'Original data',markersize = 10)
plt.scatter(x,y,s=40,c = 'none',edgecolors='k',marker = 'p',label = 'Original data')
plt.plot(x,reg.predict(x),'r',label = 'Fitted line')
plt.xlabel("Car speed")
plt.ylabel("Car dist")
plt.legend()
plt.show()

