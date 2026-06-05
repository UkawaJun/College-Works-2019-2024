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
class Graph:
    def __init__(self,graph,size,number):
        self.graph = 0
        if(graph == 'b'):
            self.graph = 1
        elif(graph == 'l'):
            self.graph = 2
        elif(graph == 's'):
            self.graph = 3
        elif(graph == 'p'):
            self.graph = 4
        else:
            self.graph = 0
            
        if self.graph == 2:
            self.crilen = size/2
        elif self.graph == 0:
            self.crilen = 0
        else:
            self.crilen = size
        self.pen = turtle.Pen()    
        self.bcol = [1.0,1.0,1.0]
        self.fcol = [0.0,0.0,1.0]
        self.number = number
        self.x = 0.0
        self.y = 0.0
        self.shade = 0.0
        self.sit =0.8
    def draws(self):
        pen = self.pen
        if(self.graph == 1):
            pen.penup()
            pen.goto(self.x - self.crilen/ 2,self.y- self.crilen/ 2)
            pen.pendown()
            pen.color(tuple(self.bcol))
            pen.pencolor(tuple(self.fcol))
            pen.pensize(3)
            pen.begin_fill()
            pen.forward(self.crilen)
            pen.left(90)
            pen.forward(self.crilen)
            pen.left(90)
            pen.forward(self.crilen)
            pen.left(90)
            pen.forward(self.crilen)
            pen.left(90)
            pen.pensize(1)
            pen.end_fill()
        
            
        elif(self.graph == 2):
            scale = self.crilen
            tacol = self.bcol
            locat = [self.x,self.y]
            sit = self.sit
            
            locat[1] -= scale
            siti = int(sit * scale) + 1
            print(siti)
            bliv =(scale / siti)
            wall = 3 / bliv
            for ran in range(0,siti):  
                a0 = siti - ran
                tur = (p1tovi(1.0,a0,siti,tacol[0]),p1tovi(1.0,a0,siti,tacol[1]),p1tovi(1.0,a0,siti,tacol[2]))
                if ran  < wall:
                    tur = ((1.0 - tacol[0])/3,(1.0 - tacol[1])/3,(1.0 - tacol[2])/3)
                draw_cri(pen,scale - ran*bliv,tur,tur,locat[0],locat[1]+ bliv*(ran + 1))
            
        elif(self.graph == 4 ):
            pen.penup()
            pen.goto(self.x,self.y)
            pen.pendown()
            pen.dot(8,(0,0,0))
            pen.dot(5,tuple(self.bcol))
            pen.penup()
            
    def line(self,loc1= [0,0],psize = 4):
        pen = self.pen
        col = self.bcol
        loc0 = [self.x,self.y]
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
    def clear(self):
        self.pen.clear()
    def can_color(self,color,shade = 0.0,fcol = [0.0,0.0,1.0]):
        sar = (1.0 - shade)/1.0
        self.bcol[0] =  (0.1 + color[0]*sar/255)/1.1
        self.bcol[1] =  (0.1 + color[1]*sar/255)/1.1
        self.bcol[2] =  (0.1 + color[2]*sar/255)/1.1
    def showloc(self,num = 3,fontsize = 20):
        
        self.pen.write('x:['+str( float(int(self.x*(10**num))/(10**num))) + ']', font =("Courier",fontsize,"bold"))
        self.pen.goto(self.x + fontsize * 0.5,self.y - fontsize * 1.5)

        self.pen.write('y:['+str( float(int(self.y*(10**num))/(10**num)))+ ']', font =("Courier",fontsize,"bold"))
        self.pen.goto(self.x - fontsize * 0.5,self.y + fontsize * 1.5)
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
#标定速度V 既循环内的变化等于 V* dt
turtle.penup()
turtle.pensize(2)
turtle.speed(0)
a0 = Graph('p',80,0)
a0.can_color([200,20,40])
turtle.tracer(False)
i = [-250.0]
i2 = [0.0]
#turtle.ht()
dt = 0
list_xy0 = [0,0]
list_xy1 = [-100,-150]
V = 10
###


#1seconds
ca = time.time()
time.sleep(1)
o1sec = time.time() - ca
###
di = 0.173915
dt = 0.00008

cst = time.time()
while(True):

    ###
    #渲染更新
    turtle.tracer(False)        #放到此处意思是在清空乃至绘制的步骤都不更新，只有画完才更新

    turtle.clear()
    a0.clear()

    ds = V*(dt/o1sec)/di     #根据平均偏差求
    c0 = time.time()
    ####################
    #绘制更新
    #turtle.shape('square')
    a0.draws()
    #a0.line([100,100],5)
   
    
    a0.showloc(3,10)

    #pen.onclick(baba, 1)
    #turtle.onscreenclick(baba,1,False)
    ####################
    turtle.tracer(True)
    #parafunc_te(list_xy0,0.3,i)\
    
    ##################
    #时间性的数值更新
    c1 = time.time()
    dt = c1 - c0
    a0.x += ds
    a0.y += ds
    if(a0.y > 40):
        input()
    #print('速度',ds)
    #print('速度V',ds/((dt)/o1sec))
    print('经理了',(time.time()- cst)/o1sec)


