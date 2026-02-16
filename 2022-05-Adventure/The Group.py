#########地图数据等
from PIL import Image

import numpy as np
from object import *
I = Image.open('pgl/G.png') 
#I.show()    
#I.save('./save.png')
I_array = np.array(I)
print(I_array.shape)
print(len(I_array),len(I_array[0]))#I_array.shape
print(I_array)
print("------------------------------------")
#for a in I_array:
#	print(a)
print(line_angle([0,0],[-1,3]))
pci = {}
print("+++++++++++++++++++++++++++++++++++++++++++")
(PIC_index('pgl/G.png',pci))
PIC_index('pgl/G.png',pci)
PIC_index('pgl/image0.png',pci)
print(pci)
