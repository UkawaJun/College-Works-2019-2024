
from ZFold import *


w = pd.read_csv("cars.csv")
x = np.array(w['speed']).reshape(-1,1)
y = np.array(w['dist']).reshape(-1,1)


from sklearn import  linear_model
reg = linear_model.LinearRegression()
n = len(y)
z = 10
zid = RFold(n,z,1010)
y_pred = RCV(reg,x,y,zid)
nmse = np.sum((y - y_pred)**2) / sum(y - np.mean(y)**2)
print(nmse)