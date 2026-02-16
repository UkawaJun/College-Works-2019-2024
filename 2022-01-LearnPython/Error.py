

#1函数外使用函数内的变量
#@NameError
def sunset():
    angles2 += 2
    if angles2 >= 360.0:
       angles2 = 0.0

while True:
    sunset()
    print(angles2)

#2函数内使用外部全局变量
#@UnboundLocalError
angle = 0.000
def sunset():
    angles += 2.0   #表示未初始化就赋值的不和谐
    if angles >= 360.0:
       angles = 0.0
    print(angles)
sunset()
#3 表示小数的取整都是从小数点开始右侧全部丢弃的
fol = -1.900166
inti = int(fol)
print(inti)