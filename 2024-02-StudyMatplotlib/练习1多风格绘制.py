import numpy as np
import matplotlib.pyplot as plt


xa = np.linspace(0,50,50)
xb = np.random.randint(40,60,50)
xc = np.random.randint(40,60,50)
xc.sort()
fig,axe = plt.subplots()

#plt.plot(xa,xb,'k-',ms = 5,mfc ='red',linewidth =3)
#plt.bar(xa,xb,width = 0.3)
axe.scatter(xa,xb,cmap = 'hot',c = xb/10,s =8)
#axe.scatter(xa,xc,cmap = 'gray',c = xb/10,s = 15)
#axe.hist(xa,xb)
axe.axis([0,50,20,80])

plt.show()
