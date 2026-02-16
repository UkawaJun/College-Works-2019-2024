
import matplotlib.pyplot as plt
import numpy as np

#imshow

x = np.linspace(0,10,1000)
I = np.sin(x)*np.cos(x).reshape(-1,1)

plt.imshow(I,cmap='afmhot_r')
#plt.imsave("hot.png",I)
plt.colorbar()
plt.show()
