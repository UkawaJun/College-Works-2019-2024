import turtle
import math
def sinti(pen):
    pen.speed(0.5)
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
def parafunc_cO(list_of_loc,t_speed,t,th):
    list_of_loc[0] = int(th/5 * math.cos(t[0]))
    list_of_loc[1] = int(th/5 * math.sin(t[0]))
    t[0] = t[0] + 1 * t_speed
def tovi(float0,now,end,bilv):      #比率水槽法
    return float0* float(1.0 - bilv* float(now/end))
#def 光线折射率普及度
def p1tovi(float0,now,end,bliv,start = 0.2):
    #bilv代表的是最后遗留的值
    s = start**(-1)     #x**-1
    blex = (bliv*s)**(-1)
    return float0 * float(float(((now/end) * (blex - start)  + start)**(-1))/s)
    
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
def dCatom(pen,tarcols = [0.8,0.8,0.8],r= 10,xy = [0,0],res = 0.08,pcol = [1,1,1]):
    tarcol = [0.0,0.0,0.0]
    tarcol[0] =  (1.1 - tarcols[0]/255)/1.1
    tarcol[1] =  (1.1 - tarcols[1]/255)/1.1
    tarcol[2] =  (1.1 - tarcols[2]/255)/1.1
    intip = xy
    t_speed = res
    t = [0.0]
    lock = [0,0]   #t的状态函数变化坐标
    t_size = int((5*r)/t_speed) + 1
    for in0 in range(0,t_size - 10):
        parafunc(lock,t_speed,t)
        pen.pencolor((tovi(pcol[0],in0,t_size,tarcol[0]),
                      tovi(pcol[1],in0,t_size,tarcol[1]),tovi(pcol[1],in0,t_size,tarcol[2])))
        pen.goto(lock[0] + intip[0],lock[1]+intip[1])
        pen.pendown()
    pen.penup()
    pcol = [0.2,0.2,0.2]
    t_size = int((5*1.45)/t_speed) + 1
    th = t[0]
    pen.pensize(3)
    tarcol = [0.0,0.0,0.0]
    for in0 in range(0,t_size - 10):
        parafunc_cO(lock,t_speed,t,th)
        pen.pencolor((tovi(pcol[0],in0,t_size,tarcol[0]),
                      tovi(pcol[1],in0,t_size,tarcol[1]),tovi(pcol[1],in0,t_size,tarcol[2])))
        pen.goto(lock[0] + intip[0],lock[1]+intip[1])
        pen.pendown()
    pen.penup()
def pdCatom(pen,tarcols = [100,100,100],pliv = 1.3,r= 10,xy = [0,0],res = 0.08,pcol = [1,1,1]):
    tarcol = [0.0,0.0,0.0]
    tarcol[0] =  (0.1 + tarcols[0]/255)/1.1
    tarcol[1] =  (0.1 + tarcols[1]/255)/1.1
    tarcol[2] =  (0.1 + tarcols[2]/255)/1.1
    intip = xy
    t_speed = res
    t = [0.0]
    lock = [0,0]   #t的状态函数变化坐标
    t_size = int((5*r)/t_speed) + 1
    for in0 in range(0,t_size - 10):
        parafunc(lock,t_speed,t)
        pen.pencolor((p1tovi(pcol[0],in0,t_size,tarcol[0],pliv),
                      p1tovi(pcol[1],in0,t_size,tarcol[1],pliv),p1tovi(pcol[1],in0,t_size,tarcol[2],pliv)))
        pen.goto(lock[0] + intip[0],lock[1]+intip[1])
        pen.pendown()
    pen.penup()
    pcol = [0.2,0.2,0.2]
    t_size = int((5*1.45)/t_speed) + 1
    th = t[0]
    pen.pensize(3)
    tarcol = [0.0,0.0,0.0]
    for in0 in range(0,t_size - 10):
        parafunc_cO(lock,t_speed,t,th)
        pen.pencolor((tovi(pcol[0],in0,t_size,tarcol[0]),
                      tovi(pcol[1],in0,t_size,tarcol[1]),tovi(pcol[1],in0,t_size,tarcol[2])))
        pen.goto(lock[0] + intip[0],lock[1]+intip[1])
        pen.pendown()
    pen.penup()

def stick(pen,loc0 = [0,0],loc1= [0,0],col = [1.0,1.0,1.0],psize = 4):
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
    
drawXY(0,0,40,2)
pen = turtle.Pen()
pen.penup()
turtle.bgcolor((0.4,0.4,0.5))
pen.pensize(2)
pen.speed(0.5)          #!

#time = (r * 5)/t_speed
#####
stick(pen,[40,-40],[40,0])
stick(pen,[80,-40],[40,-40])
pdCatom(pen,[50,47,156],1.9,20,[40,-40])
dCatom(pen,[50,47,156],20,[80,-40])

########


pen.ht()
