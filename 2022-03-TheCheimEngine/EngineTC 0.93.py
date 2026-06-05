import turtle
import math
import time
import turtle

mxy = [0,0]
pov = [0.0,0.0]
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
    def __init__(self,graph,size,number,center = False,dxy = [0.0,0.0],color = [150,100,150]):
                #   形状  大小  编号（None）  中心化    位置
        self.graph = 0
        self.blocks = 0
        
        if center:
            self.struct = [self]
            self.blocks = 1
        else:
            self.struct = [None]    #为None则一定不允许插入新结构
            self.blocks = 0
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
        self.pen.ht()
        self.bcol = [1.0,1.0,1.0]   #背景色
        self.fcol = [0.0,0.0,1.0]   #画笔色
        self.number = number        #编号
        self.x = dxy[0]                #相对组别的偏移量
        self.y = dxy[1]                
        self.can_color(color)
        self.shade = 0.0            #画圆用的参数
        self.sit =0.8
        #Active
        self.ax = 0.0               #运动量
        self.ay = 0.0
        self.a_x = 0.0              #加速度
        self.a_y = 0.0

        self.v_ax = 0.0             #速度量
        self.v_ay = 0.0
        self.v_x = 0.0              #初始速度
        self.v_y = 0.0
        # Group struct active
        self.tgth = True
        self.center = center
    def _insert(self,graph):
        if self.struct[0] == None:
            return 0;
        else:
            for a in graph:
                self.struct.append(a)
    def _reloc(self):
        return [self.x +self.ax,self.y +self.ay]
    def draws(self,widov = 1):
        pen = self.pen
        if(self.graph == 1):    #block
            pen.penup()
            (self.x + self.ax)
            pen.goto((self.x + self.ax)  - self.crilen* widov/ 2,
                     (self.y + self.ay)- self.crilen/ 2)
            pen.pendown()
            pen.color(tuple(self.bcol))
            pen.pencolor(tuple(self.fcol))
            pen.pensize(3)
            pen.begin_fill()
            pen.forward(self.crilen * widov)
            pen.left(90)
            pen.forward(self.crilen)
            pen.left(90)
            pen.forward(self.crilen * widov)
            pen.left(90)
            pen.forward(self.crilen)
            pen.left(90)
            pen.pensize(1)
            pen.end_fill()  
        elif(self.graph == 2): #cricle
            scale = self.crilen
            tacol = self.bcol
            locat = [(self.x + self.ax),(self.y + self.ay)]
            sit = self.sit
            
            locat[1] -= scale
            siti = int(sit * scale) + 1
            #print(siti)
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
            pen.goto((self.x + self.ax),(self.y + self.ay))
            pen.pendown()
            pen.dot(8,(0,0,0))
            pen.dot(5,tuple(self.bcol))
            
        pen.penup()
    def line(self,loc1= [0,0],psize = 4):
        pen = self.pen
        col = self.bcol
        loc0 = [(self.x + self.ax),(self.y + self.ay)]
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
        if self.center:
            self.pen.clear()
            for a in self.struct:
                if a == self:
                    continue
                a.pen.clear()
                if a.center:
                    a.clear()
                
        else:
            self.pen.clear()

    def can_color(self,color,shade = 0.0,fcol = [0.0,0.0,1.0]):
        sar = (1.0 - shade)/1.0
        self.bcol[0] =  (0.1 + color[0]*sar/255)/1.1
        self.bcol[1] =  (0.1 + color[1]*sar/255)/1.1
        self.bcol[2] =  (0.1 + color[2]*sar/255)/1.1

    def nagative_color(self):
        self.bcol[0] = 1.0 - self.bcol[0]
        self.bcol[1] = 1.0 - self.bcol[1]
        self.bcol[2] = 1.0 - self.bcol[2]
    def showloc(self,num = 3,fontsize = 20):     
        self.pen.write('x:['+str( float(int((self.x + self.ax)*(10**num))/(10**num))) + ']', font =("Courier",fontsize,"bold"))
        self.pen.goto((self.x + self.ax) + fontsize * 0.5,(self.y + self.ay) - fontsize * 1.5)
        self.pen.write('y:['+str( float(int((self.y + self.ay)*(10**num))/(10**num)))+ ']', font =("Courier",fontsize,"bold"))
        self.pen.goto((self.x + self.ax) - fontsize * 0.5,(self.y + self.ay) + fontsize * 1.5)
    def showfont(self,str0,num = 3,fontsize = 15):
        self.pen.goto((self.x + self.ax) - fontsize * 3,(self.y + self.ay) - fontsize * 1)
        self.pen.write(str0, font =("Courier",fontsize,"bold"))
        self.pen.goto((self.x + self.ax) + fontsize * 3,(self.y + self.ay) + fontsize * 1)
    def active(self,time):
        self.ax = self.v_x *time  + (1/2)*self.a_x * (time**2)         
        self.ay = self.v_y *time  + (1/2)*self.a_y * (time**2) 
        self.v_ax = self.v_x + self.a_x *time         #速度的变化量
        self.v_ay = self.v_y + self.a_x *time
    def active_cri(self,time,cri = 30,sloc = [0,0]):
        self.ax = math.cos(time)*cri +sloc[0]
        self.ay = math.sin(time)*cri +sloc[1]
    def ch_moveto_objlim(self,gra,speed = 0.05):
        x = gra.x +gra.ax - (self.x + self.ax)
        y = gra.y +gra.ay - (self.y + self.ay)
        x *= speed
        y *= speed
        self.ax += x
        self.ay += y
        self.struct_kanst(x,y)
    def struct_draw(self,dself = True):
        ints = 0
        for a in self.struct:
            ints += 1
            if a == self:
                if not dself:
                    continue
            a.draws()
            if a.center :
                a.struct_draw(False)
        print(ints)
    def struct_kanst(self,ax,ay):
        if not self.center:
            return 0
        if not self.tgth:
            return 0
        for a in self.struct:
            if a == self:
                continue
            a.ax += ax
            a.ay += ay
            if a.center :
                a.struct_kanst(ax,ay)

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
    turtle.bgcolor((63/255,127/255,165/255))

#ca = time.time()
#time.sleep(1)
#o1sec = time.time() - ca    

screen0 = turtle.Screen()
screen0.setup(1500,500)
def funx():
    screen0.bye()
turtle.bgcolor((63/255,127/255,165/255))
turtle.delay(0)    
drawXY(0,0,40,10)
#标定速度V 既循环内的变化等于 V* dt
turtle.ht()
turtle.penup()
turtle.pensize(2)
turtle.speed(0)
##
a0 = Graph('p',180,0)
a0.can_color([200,20,240])
a1 = Graph('b',40,1)
a1.can_color([40,120,220])
a0.v_y = 10
a0.a_y = -2.5
a0.v_x = 20
a0.a_x = -5

stru1 = Graph('p',1,0,True,[0,100])
#按钮 添加可以直接列表化
button = [Graph('b',40,20,False,[-500,40]),
          Graph('b',40,20,False,[-500,-100])]
button[1].can_color([200,20,40])
#
stru1._insert([Graph('b',30,0,False,[180,180]),
                Graph('b',30,0,False,[-180,180]),
                Graph('b',30,0,True,[-180,-180]),
                Graph('b',30,0,True,[180,-180])])
stru1.struct[4]._insert([Graph('b',20,0,False,[220,-220]),
                Graph('b',20,0,False,[220,-140],[100,230,20]),
                Graph('b',30,0,False,[140,-140],[100,230,230]),
                Graph('l',30,0,False,[140,-220],[200,30,20])])
stru1.struct[3]._insert([Graph('b',20,0,False,[220,-220]),
                Graph('b',20,0,False,[220,-140],[100,230,20]),
                Graph('b',30,0,False,[140,-140],[100,230,230]),
                Graph('b',30,0,False,[140,-220],[200,30,20])])
for a in range(1,5):
    stru1.struct[a].can_color([(a*(255/4)),(a*(255/4)),(a*(255/4))])
    stru1.struct[a].fcol = [(a*(255/4))/255,(a*(255/4))/255,(a*(255/4))/255]
    stru1.struct[a].nagative_color()

###Time  &&Fps
bool_t = [False,True]
di = 1.68915        #None
dt = 0
ds = 0
dxs = 0.0
cst = time.time()
stop = 0.0
fps = 0
tfps = 0

###Time
###9.30###
the2 = Graph('b',20,1,True,[100,100],[255,100,200])
the2._insert([Graph('b',20,1,True,[-100,100],[255,100,10])])

def funt():
    if bool_t[0]:
        button[0].nagative_color()
        bool_t[0] = False
    else:
        button[0].nagative_color()
        bool_t[0] = True
def check_events(screen0):    
    screen0.onkey(funx,'x')
    screen0.onkey(funt,'t')
    screen0.listen()
while(True):
    
    if not bool_t[0]:
        #渲染更新
        turtle.tracer(False)  #清理过程再到第二次绘制的过程完全不呈现出来   
        turtle.clear()
        a0.pen.clear()
        for a in button:
            a.clear()
        stru1.clear()
        the2.clear()

        c0 = time.time()
        #
        #绘制更新
        #turtle.shape('square')
        a0.line([-100 ,100],5)

        for a in stru1.struct:
            a.line(stru1._reloc(),5)
        for b in stru1.struct[4].struct:
            b.line(stru1.struct[4]._reloc(),4)
        stru1.struct_draw()
        for a in range(1,5):
            if a == 4:
                stru1.struct[a].ch_moveto_objlim(stru1.struct[1],0.003)
            else:
                stru1.struct[a].ch_moveto_objlim(stru1.struct[a+1],0.003)
        sts = stru1.struct[4].struct
        for a in range(1,5):
            if a == 4:
                sts[a].ch_moveto_objlim(sts[1],0.003)
            else:
                sts[a].ch_moveto_objlim(sts[a+1],0.003)
        
        stru1.ch_moveto_objlim(a0,0.051)                                                                           
        a0.draws()
        #a0.nagative_color()

        the2.struct_draw()
        the2.ch_moveto_objlim(a0,0.001)
        the2.line(the2.struct[1]._reloc())

        ###############################
        for a in button:
            a.draws(4.3)

            #Time
        button[0].showfont('(t):['+ str(float(int(dxs*100)/100)) + ']',2)
            #Fps
        button[1].showfont('Fps['+ str(tfps) + ']',3)
        a0.showloc(3,10)
        
        
        #button[0].pen.write('Time:['+str(float(int(dxs*100)/100))+ ']', font =("Courier",15,"bold"))
        #pen.onclick(baba, 1)
        #turtle.onscreenclick(baba,1,False)
        ####################
        turtle.tracer(True)
        c1 = time.time()
        dt = c1 - c0
        dxs = ((time.time()- cst - stop))    #Time throught
        a0.active_cri(dxs,60)
        check_events(screen0)

        fps += 1;
        if((dxs%1)< 0.5 and bool_t[1]):
            tfps = fps
            fps = 0
            bool_t[1] = False
        if (dxs%1) > 0.5:
            bool_t[1] = True
       
    else:
        c0 = time.time()
        turtle.tracer(False)
        
        for a in button:
            a.draws(4.3)
        button[0].showfont('(t):['+ str(float(int(dxs*100)/100)) + ']',2)
        turtle.tracer(True) 
        check_events(screen0)
        c1 = time.time()
        dt = c1 - c0
        stop += dt              
        #stop 意味着储存暂停的全部时刻 这样才能中和时间差
        #所以在运行中的意味着时间差上并不会有误差
    

   