#init
import turtle
inti = True

flie = 'data.txt'
if not inti:
	with open(flie,'w') as m:
		m.write("")
datas = ''
with open(flie,'r') as m:
	datas = m.read()
dal = []
for a in datas.split(" "):
	dal.insert(-1,int(a))
dal.insert(0,0)

dab = sorted(dal)
_max = dab[-1]
_min = dab[0]
_n = len(dab)
print(dal,dab)
print(_max,_min)

screen = [600,600]
screen0 = turtle.Screen()
screen0.setup(screen[0],screen[1],0,0)
#起始坐标左偏 偏移量
oriloc = screen[0]*(4/5)/2
turtle.bgcolor((189/255,103/255,93/255))

pa = turtle.Pen()
#pa.ht()
pa.pu()
pa.goto(-oriloc,0)


def drawXY(_n,b_size):
	pa.goto(-oriloc,-oriloc)
	pa.pensize(4)
	pa.speed(0)
	pa.pd()
	pa.color((0.7,0.9,0.7))
	for a in range(0,_n):
		pa.left(90)	; pa.fd(b_size)
		pa.right(90)  ; pa.fd(b_size*_n)
		pa.pu()    ;   pa.fd(-b_size*_n)
		pa.pd()
	pa.goto(-oriloc,-oriloc)

	for a in range(0,_n):
		pa.fd(b_size) ;		pa.left(90)
		pa.fd(b_size*_n);	pa.pu()
		pa.fd(-b_size*_n);	pa.right(90);
		pa.pd()
	pa.goto(-oriloc,-oriloc)
	pa.color((1.0,0,0))
	pa.fd(b_size*_n);
	pa.goto(-oriloc,-oriloc)
	pa.left(90)
	pa.color((0,0,1.0))
	pa.fd(b_size*_n)
	pa.goto(-oriloc,-oriloc)
	pa.right(90)
	pa.pu()

def nagative_color(sel):
	bcol = [0.0,0.0,0.0]
	bcol[0] = 1.0 - sel[0]
	bcol[1] = 1.0 - sel[1]
	bcol[2] = 1.0 - sel[2]
	return bcol

def drawData(_n,sizeb,bsize ,bcol = [1.0,1.0,1.0]):
	pa.goto(-oriloc,-oriloc)
	pa.color(bcol)
	
	pa.pd()
	pa.speed(0)
	print(dal[0])
	for a in range(0,_n):
		pa.goto(-oriloc + a*(bsize),-oriloc)
		pa.left(90);	
		pa.goto(-oriloc + a*(bsize),-oriloc +sizeb*dal[a])
		pa.pu();
		pa.goto(-oriloc + a*(bsize),-oriloc)
		pa.right(90); 
		
		pa.pd();
	for a in range(0,_n):
		pa.pu();
		pa.goto(-oriloc + a*(bsize),-oriloc)
		pa.left(90);

		pa.goto(-oriloc + a*(bsize),-oriloc +sizeb*dal[a])
		pa.pd()
		pa.pencolor(nagative_color(bcol))
		pa.write(dal[a], font =("Courier",14,"bold"))
		pa.pencolor(bcol)
		pa.pu()
		pa.goto(-oriloc + a*(bsize),-oriloc)
		pa.right(90); 
		
	
	
#计算网格长度 大小
bsize = (oriloc*2.0) / _n
sizeb = (oriloc*2.0)/(_max - _min)

drawXY(_n,bsize)
drawData(_n,sizeb,bsize,bcol =(0,0,0))
input()

