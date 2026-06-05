import turtle
import math
import time
mxy = [0,0]
def draw_cri(pen,cri_size,fcol,bcol,x,y):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.color(bcol)
    pen.begin_fill()
    pen.pencolor(fcol)
    pen.pensize(1)
    pen.circle(cri_size)
    pen.end_fill()
def draw_block(pen,lens,fcol,bcol,x,y):
    pen.penup()
    pen.goto(x - lens/ 2,y- lens/ 2)
    pen.pendown()
    pen.color(bcol)
    pen.pencolor(fcol)
    pen.pensize(3)
    pen.begin_fill()
    pen.forward(lens)
    pen.left(90)
    pen.forward(lens)
    pen.left(90)
    pen.forward(lens)
    pen.left(90)
    pen.forward(lens)
    pen.left(90)

    pen.pensize(1)
    pen.end_fill()
def loc_can(t,x,y):     #改变坐标位置 具有严谨的过程
    t.penup()
    t.goto(x,y)
    t.pendown()
def drf(t,leng):     #改变坐标位置 具有严谨的过程
    t.pendown()
    t.forward(leng)
    t.penup() 
#def 光线折射率普及度 积累过程是正向的 
def p1tovi(float0,now,end,bliv,start = 0.2):
    #bilv代表的是最后遗留的值
    s = start**(-1)     #x**-1
    blex = (bliv*s)**(-1)
    return float0 * float(float(((now/end) * (blex - start)  + start)**(-1))/s)
def draws_cri(pen,locat,tacol = [100,100,100],scale = 10,shade = 0.0,sit =0.8):
 #locat位置坐标列表# tacol目标的颜色列表  # siti为分辨率 最大效率即： 不要画重复的
    locat[1] -= scale
    sar = (1.0 - shade)/1.0
    tacol[0] =  (0.1 + tacol[0]*sar/255)/1.1
    tacol[1] =  (0.1 + tacol[1]*sar/255)/1.1
    tacol[2] =  (0.1 + tacol[2]*sar/255)/1.1 
    siti = int(sit * scale) + 1
    print(siti)
    bliv =(scale / siti)
    wall = 3 / bliv
    for ran in range(0,siti):  
        a0 = siti - ran
        tur = (p1tovi(1.0,a0,siti,tacol[0]),p1tovi(1.0,a0,siti,tacol[1]),p1tovi(1.0,a0,siti,tacol[2]))
        if ran  < wall:
            tur = (0.2,0.1,0.1)
        draw_cri(pen,scale - ran*bliv,tur,tur,locat[0],locat[1]+ bliv*(ran + 1))
#参数函数系列
def rett(size,t,tsqa = 1):      #3t**-9 的结果
    return size*(t**tsqa) 
def parafunc(list_of_loc,t_speed,t):
    list_of_loc[0] = int(t[0]/5 * math.cos(t[0]))
    list_of_loc[1] = int(t[0]/5 * math.sin(t[0]))
    t[0] = t[0] + 1 * t_speed
def parafunc_cO(list_of_loc,t_speed,t,th):
    list_of_loc[0] = int(th/5 * math.cos(t[0]))
    list_of_loc[1] = int(th/5 * math.sin(t[0]))
    t[0] = t[0] + 1 * t_speed
def parafunc_te(list_of_loc,t_speed,t):
    list_of_loc[0] = int(40 * math.cos(t[0]))
    list_of_loc[1] = int(40 * math.sin(t[0]))
    t[0] = t[0] + 1 * t_speed
def parafunc_e(list_of_loc,t_speed,t):
    list_of_loc[0] = t[0]
    list_of_loc[1] =  (math.e**-t[0])
    t[0] = t[0] + 1 * t_speed
def parafunc_x2(list_of_loc,t_speed,t):
    list_of_loc[0] = t[0]
    list_of_loc[1] =  (t[0]**2 / 350 ) + 15
    t[0] = t[0] + 1 * t_speed
def tovi(float0,now,end,bilv):      #比率水槽法
    return float0* float(1.0 - bilv* float(now/end))
####
def drawXY(intix,intiy,unit,size):
    lip = [turtle.Pen(),turtle.Pen(),turtle.Pen(),turtle.Pen()]
    for ra in range(0,4):
        lip[ra].left(ra * 90)
        loc_can(lip[ra],intix,intiy)
        lip[ra].pencolor('white')
        lip[ra].pensize(2)
        lip[ra].speed(0)
    for ra in range(0,size):
        for te in lip:
            drf(te,unit)
            te.left(90)
            drf(te,unit*size)
            drf(te,-2*unit*size)
            drf(te,unit*size)
            te.right(90)
    for ra in range(0,4):
        loc_can(lip[ra],intix,intiy)
        if(ra == 0 or ra == 2):
            lip[ra].pencolor('red')
        else:
            lip[ra].pencolor('blue')
        lip[ra].pensize(3)
        lip[ra].speed(0)
    for ra in range(0,size+1):
        for te in lip:
            drf(te,unit)
            te.left(90)
            drf(te,5)
            drf(te,-5)
            te.right(90)
    for ra in lip:
        ra.ht()
def stick(pen,loc0 = [0,0],loc1= [0,0],col = [1.0,1.0,1.0],psize = 4):
    pen.speed(1)
    if(psize < 2):
        psize = 2
    pen.pencolor((col[0],col[1],col[2]))
    pen.penup()
    pen.pensize(psize)
    pen.goto(loc0[0],loc0[1])
    pen.pendown()
    pen.goto(loc1[0],loc1[1])
    pen.pensize(psize - 1)
    pen.pencolor((col[0]/2,col[1]/2,col[2]/2))
    pen.goto(loc0[0],loc0[1])
    pen.penup()
def baba(xdummy, ydummy):
    #turtle.goto(xdummy, ydummy)
    mxy[0] = xdummy
    mxy[1] = ydummy
    turtle.bgcolor((20/255,20/255,93/255))
screen0 = turtle.Screen()
screen0.setup(500,500)
turtle.bgcolor((189/255,103/255,93/255))
turtle.delay(0)    
drawXY(0,0,40,10)
pen = turtle.Pen()
pen.penup()

pen.pensize(2)
pen.speed(0)

turtle.tracer(False)
i = [-250.0]
i2 = [0.0]
#pen.ht()
dt = 0
list_xy0 = [0,0]
list_xy1 = [-100,-150]
while(True):
    
    turtle.tracer(False)        #放到此处意思是在清空乃至绘制的步骤都不更新，只有画完才更新
    #time.sleep(0.00)
    pen.clear()
    
    c0 = time.time()
    ###
    
    ###
    stick(pen,[list_xy0[0],list_xy0[1]+80],[list_xy0[0]-60,list_xy0[1] -35],[1.0,1.0,0],5)
    stick(pen,[list_xy0[0],list_xy0[1]+80],[list_xy0[0]+60,list_xy0[1] -35],[1.0,0,1.0],5)
    stick(pen,[list_xy0[0]-60,list_xy0[1] -35],[list_xy0[0]+60,list_xy0[1] -35],[0,1.0,1.0],5)

    stick(pen,[list_xy0[0],list_xy0[1]-80],[list_xy0[0]-60,list_xy0[1] +35],[0,1.0,0],5)
    stick(pen,[list_xy0[0],list_xy0[1]-80],[list_xy0[0]+60,list_xy0[1] +35],[0,0,1.0],5)
    stick(pen,[list_xy0[0]-60,list_xy0[1] +35],[list_xy0[0]+60,list_xy0[1] +35],[1.0,0,0],5)
    ###
    draws_cri(pen,[list_xy0[0],list_xy0[1]+80],[250,0,0],20,0.3,1.2)
    draws_cri(pen,[list_xy0[0]-60,list_xy0[1] -35],[0,250,0],20,0.4,1.2)
    draws_cri(pen,[list_xy0[0]+60,list_xy0[1] -35],[0,0,255],20,0.5,1.2)
    
    draws_cri(pen,[list_xy0[0],list_xy0[1]-80],[0,255,255],20,0.45,1.2)
    draws_cri(pen,[list_xy0[0]-60,list_xy0[1] +35],[255,255,0],20,0.35,1.2)
    draws_cri(pen,[list_xy0[0]+60,list_xy0[1] +35],[255,0,255],20,0.8,1.2)
    ###偏移
    
    pen.shape('square')
    
    draw_block(pen,160,(0,0,0),(1,1,0),mxy[0] + int(i[0]),mxy[1])
    pen.write(str(i), font = ("Courier", 20, "bold") )
    
    pen.onclick(baba, 1)
    #turtle.onscreenclick(baba,1,False)
    ###
    turtle.tracer(True)
    #变化的过程使用不同的i预示着
    #变化速率的不同和运行轨迹，参照系的不同
    #且使用同一个坐标表(list_xy)的
    #仅仅在该该坐标中心发生偏移即可一起运动
    parafunc_te(list_xy0,1,i)
    parafunc_te(list_xy1,0.2,i2)
    c1 = time.time()
    print(c1 -c0)
    dt = c1 - c0

    


