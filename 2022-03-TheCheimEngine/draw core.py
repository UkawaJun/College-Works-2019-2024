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

def loc_can(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def returple(fcol,range0,ran):
    return (fcol[0]*((range0 -ran)/range0),fcol[1]*((range0 -ran)/range0),
            fcol[2]*((range0 -ran)/range0))
def draws_cri(pen,list_fcol,list_loccc,range0,scale):
    loccc = list_loccc
    fcol = list_fcol
    for ran in range(0,range0):
        draw_cri(pen,scale - 2*ran,returple(fcol,range0,ran),returple(fcol,range0,ran),
                 loccc[0],loccc[1])
        loc_can(pen,loccc[0],loccc[1])
    
def parafunc(list_of_loc,t_speed,t):
    list_of_loc[0] = int(t[0] * math.cos(t[0]))
    list_of_loc[1] = int(100 * math.sin(t[0]))
    t[0] = t[0] + 1 * t_speed
   
t = turtle.Pen()
#turtle.fillcolor("black") 
fcol = [0.9,0.3,0.4]
sinti(t)
scale = 3; copi = 0.3;     # copi < 0.5
range0 = int(scale * copi)
#draws_cri(t,[0.5,0.3,0.8],[-100,-90],range0,scale)
#draws_cri(t,[0.9,0.3,0.8],[100,-90],range0,scale)
#loc_can(t,180,180)
rt = [0.0]
t_speed = 0.1
lisoloc = [0,0]
for ran0 in range(0 ,400):      #其实是t参数函数的取值范围
    
    draws_cri(t,[0.4,0.8,0.8],lisoloc,range0,scale)
    t.pendown()
    t.pencolor([0.1,0.3,0.2])
    t.pensize(2)
    parafunc(lisoloc,t_speed,rt)
    t.goto(lisoloc[0],lisoloc[1])
    t.penup()




print("ab" *2)


        
