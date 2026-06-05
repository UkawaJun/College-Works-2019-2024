import turtle
import math
def sinti(pen):
    pen.speed(0.0)
def draw_cri(pen,cri_size,fcol ,bcol,x,y):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.color(bcol)
    pen.begin_fill()
######
    pen.pencolor(fcol)
    pen.pensize(1)
    pen.circle(cri_size)
######
    pen.end_fill()

def loc_can(t,x,y):     #改变坐标位置 具有严谨的过程
    t.penup()
    t.goto(x,y)
    t.pendown()
def drf(t,leng):     #改变坐标位置 具有严谨的过程
    t.pendown()
    t.forward(leng)
    t.penup()
def returple(fcol,range0,ran,bilv):  #返回颜色组
    return (fcol[0]*((range0 -ran/bilv)/range0),fcol[1]*((range0 -ran)/range0),
            fcol[2]*((range0 -ran/bilv)/range0))    
def draws_cri(pen,list_fcol,list_loccc,range0,scale):
    loccc = list_loccc
    fcol = list_fcol
    for ran in range(0,range0):
        draw_cri(pen,scale - 2*ran,returple(fcol,range0,ran),returple(fcol,range0,ran),
                 loccc[0],loccc[1])
        loc_can(pen,loccc[0],loccc[1])
########T
def parafunc(list_of_loc,t_speed,t):
    list_of_loc[0] = int(t[0]/5 * math.cos(t[0]))
    list_of_loc[1] = int(t[0]/5 * math.sin(t[0]))
    t[0] = t[0] + 1 * t_speed
def tovi(float0,now,end,bilv):      #比率水槽法
    return float0* float((end - (now/bilv))/end)
def rett(size,t,tsqa = 1):      #3t**-9 的结果
    return size*(t**tsqa)       
def drawXY(intix,intiy,unit,size):
    lip = [turtle.Pen(),turtle.Pen(),turtle.Pen(),turtle.Pen()]
    for ra in range(0,4):
        lip[ra].left(ra * 90)
        loc_can(lip[ra],intix,intiy)
        if(ra == 0 or ra == 2):
            lip[ra].pencolor('red')
        else:
            lip[ra].pencolor('blue')
        lip[ra].pensize(3)
        lip[ra].speed(0.5)
    for ra in range(0,size+1):
        for te in lip:
            drf(te,unit)
            te.left(90)
            drf(te,5)
            drf(te,-5)
            te.right(90)
drawXY(0,0,40,9)
pen = turtle.Pen()
pen.penup()
pen.goto(40,40)
turtle.bgcolor((0.4,0.4,0.5))
t_speed = 0.08
pcol = [1,1,1]
pen.pensize(2)
pen.speed(0.5)          #!
t = [0.0]
t_size = 1800 # 次数
t_lv = 3    #比率
lock = [0,0]        #locations
intip = [40,40] 

for in0 in range(0,t_size - 10):
    parafunc(lock,t_speed,t)
    #在tovi函数中 第三参数越大，对相应的三原色的保留就越大
    pen.pencolor((tovi(pcol[0],in0,t_size,1),tovi(pcol[1],in0,t_size,1.4),tovi(pcol[1],in0,t_size,2.3)))
    pen.goto(lock[0] + intip[0],lock[1]+intip[1])
    pen.pendown()
pen.penup()

intip = [40,-40]
t = [0.0]
for in0 in range(0,t_size - 10):
    parafunc(lock,t_speed,t)
    #在tovi函数中 第三参数越大，对相应的三原色的保留就越大
    pen.pencolor((tovi(pcol[0],in0,t_size,2.3),tovi(pcol[1],in0,t_size,1.4),tovi(pcol[1],in0,t_size,1)))
    pen.goto(lock[0] + intip[0],lock[1]+intip[1])
    pen.pendown()
pen.penup()

intip = [-40,-40]
t = [0.0]
for in0 in range(0,t_size - 10):
    parafunc(lock,t_speed,t)
    #在tovi函数中 第三参数越大，对相应的三原色的保留就越大
    pen.pencolor((tovi(pcol[0],in0,t_size,1.4),tovi(pcol[1],in0,t_size,2.3),tovi(pcol[1],in0,t_size,1)))
    pen.goto(lock[0] + intip[0],lock[1]+intip[1])
    pen.pendown()
pen.penup()

intip = [-40,40]
t = [0.0]
for in0 in range(0,t_size - 10):
    parafunc(lock,t_speed,t)
    #在tovi函数中 第三参数越大，对相应的三原色的保留就越大
    pen.pencolor((tovi(pcol[0],in0,t_size,2.3),tovi(pcol[1],in0,t_size,1),tovi(pcol[1],in0,t_size,1.1)))
    pen.goto(lock[0] + intip[0],lock[1]+intip[1])
    pen.pendown()
pen.penup()


pen.ht()
