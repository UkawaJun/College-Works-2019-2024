import pyglet,random,pyglet.gl,time
from object import *
from adai import *


#from pyglet.gl import *

time_max = [0.0]
screen_trans_1 = [0.0,0.0]
mouse_trans_1 = [0.0,0.0,0.0,0.0]
change = [0]
RDT = 0.001

from pyglet.window import key
FALL_key_handler = key.KeyStateHandler()
key_board = {}
def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2


screen_size = [1600,1000]
game_window = pyglet.window.Window(screen_size[0], screen_size[1],caption = "The Adventure!",fullscreen = False)

####----------------------载入贴图-----------------------------####
index = 'pgl'
pyglet.resource.path = [index]
pyglet.resource.reindex()
main_batch = pyglet.graphics.Batch()
buls = pyglet.resource.image('buttles.png')
pla = pyglet.resource.image('PL.png')
Ani = pyglet.resource.image('A.png')
backi = pyglet.resource.image('Point.png')
apl = pyglet.resource.image('apl.jpeg')
ta = pyglet.resource.image('wall2.png')
ammow0 = pyglet.resource.image('ammow.png')
bul = [buls.get_region(0 + 4*a, 0, 3, 20) for a in range(0,8)]
####-----------------------------------------------------------####
# 定义 object --->  inti  --> update  --> product  --> draw  -- > for
#定义背景 Object
bac = Object(image= backi,x= screen_size[0]/2, y =screen_size[1]/2)
bac.image_set(4)
#定义鼠标
ammow = Object(image= ammow0,x= screen_size[0]/2, y =screen_size[1]/2)
ammow.image_set(5)



c = Object(image= Ani,x = 800, y = 500,batch = main_batch)
#######################################
pic = pyglet.image.load('pgl/G.png')
format = 'RGBA'
rawimage = pic.get_image_data()
pitch = rawimage.width * len(format)
pixels = rawimage.get_data(format, pitch)
#asr = pyglet.gui.PushButton(800,500)
print(pixels)
for a  in pixels:
    print(a , end = '  ')  
print(len(pixels[4:])/4)

#c.create_talk("Context : Start Game")
########################################
ani = Object(image= Ani,x = 900, y = 500,batch = main_batch)
walls1 = [pyglet.resource.image('wall' + str(a)+'.png') for a in range(0,4)]
wall_a = [Object(image= walls1[a %4],x = 800, y = 500,batch = main_batch) for a in range(0,8)]
for a in wall_a:
    a.image_set(0.1)

ccs = Team()
blocks = Team()
ccs.app_object([Object(image= walls1[a % 4],x = 200, y = 500,batch = main_batch) for a in range(0,8)])
for a,b in enumerate(ccs.team):
    b.scale += 1
    b.x += b.x + a*20
    b.scale = 0.8

c.create_talk("BST")
c.image_set(4)
#ani.image_setting(3,'sad')
ani.image_set(8,1)
player = Player(image= pla,x= 800, y = 500,batch = main_batch)
print(player.image_append(pyglet.resource.image('image0.png'),modle = 'rus'))
print(player.image_append(pyglet.resource.image('image1.png'),modle = 'rus'))
print(player.image_append(pyglet.resource.image('image2.png'),modle = 'rus'))
print(player.image_append(pyglet.resource.image('image3.png'),modle = 'rus'))
print(player.imagei['count'])
player.image_change(0)
asa =player.image_create('cri',color=(200,100,230),size = [40,280])
#player.boxSetCus(20,40)
#player.image_next(1)
#player.image_next(1)


#input(player.width)
#player.velocity_x = 100
players = [player]
#player.o_rotation(10)
#player.bool_list['box.open'] =  False
player.data_box()
#player.setting_box(10,10)
blocks.app_object([Object(image= walls1[a % 4],x = 100 +int(a%8)*60, y = 300 + int(a/8)*60,batch = main_batch) for a in range(0,40)])
player.objectCreates(blocks.team)
for a in blocks.team:
    a.image_set(0.5)
player.owner.bool_list['is_twins'] = True

#@game_window.event

###


pattern = pyglet.image.SolidColorImagePattern(color=(200,100,230,255))
image = pattern.create_image(150,2)
second = pyglet.sprite.Sprite(image, x=800, y=500)
second.rotation = 90
second.scale =4
#c.bool_list['box.rota'] = False
circle = pyglet.shapes.Circle(x=100, y=150, radius=40, color=(200,100,230))
c.ObjReloc(200,200)

###
def zero_time(dt):
    time_max[0] = 0.0
    pyglet.clock.schedule_once(zero_time, 2)
def check_board(key_board,FALL_key_handler):
    if FALL_key_handler[key.W]:
        key_board['w'] = True
    else:
        key_board['w'] = False

    if FALL_key_handler[key.A]:
        key_board['a'] = True
    else:
        key_board['a'] = False

    if FALL_key_handler[key.S]:
        key_board['s'] = True
    else:
        key_board['s'] = False

    if FALL_key_handler[key.D]:
        key_board['d'] = True
    else:
        key_board['d'] = False
    if FALL_key_handler[key.S]:
        key_board['s'] = True
    else:
        key_board['s'] = False

    if FALL_key_handler[key.B]:
        key_board['b'] = True
    else:
        key_board['b'] = False
    if FALL_key_handler[key.T]:
        key_board['t'] = True
    else:
        key_board['t'] = False
    if FALL_key_handler[key.J]:
        key_board['j'] = True
    else:
        key_board['j'] = False
    if FALL_key_handler[key.U]:
        key_board['u'] = True
    else:
        key_board['u'] = False
bos2 = [False]
bos3 = [False]
def on_draw():
    
   
    
    game_window.clear()
    #绘制区域#--------------------------
    #背景
    bac.draw()
    #玩家
    player.draw();
    player.owner.draws(leng = 900)
    #鼠标
    ammow.draw();
    #绘制区域#---------------

def update_mail(dt,key_board):
    #更新区域-------------------------
   
    ba = c.Objbounce(player,dt)
    i = 0

    c.ObjRota(player,dt)
    if ba:
        c.ObjTurn_object(player,dt,dir = False)     #player.owner.team_collEach(player,dt)

    #player.owner.team_collEach(player,dt)
    for a in player.owner.team:
            a.Objbounce(player,dt)
            a.Objbounce(c,dt)
            if((a.ias.last_move or a.ias.last_rota)):
                for b in player.owner.team:
                    b.Objbounce(a,dt)
                    
                    
    c.Obj_rotation(5) 
    
    #c.ObjFord(player,dt)
    
    
    #先是改变  后去赋值  这是两种改变数据的方式
    change[0] += 1 
    #c.x ,c.y = c.init_location[0],c.init_location[0]
    aa = False
    if players:
        for a in players:
            ##1改数据  2自然修改数据 3数据稳定计算碰撞箱
            a.Move_it(ammow,dt,key_board,screen_trans_1)
    
    ani.update(dt,screen_trans_1)
    bac.update(dt,screen_trans_1)
    c.update(dt,screen_trans_1)
    #print(player.ias.is_move,player.ias.is_rota)
    #print(player.ias.last_move,player.ias.last_rota)
    if players:
        for a in players:
            a.updates_4(dt)
            a.dates_itsself(dt,screen_trans_1)      
    for a in wall_a:
        a.update(dt,screen_trans_1) 
    ccs.datas(dt,screen_trans_1)  
    al = 0  
    #player.owner.team[1].x = player.owner.team[1].father[0].x - 30
    #更新区域-------------------
def protect():
    ###常用于因变换而影响物块是否删除和发生改变 比如碰撞箱就属于变化 而自身变化放在update_data
    player.owner.dled_protect()
    blocks.protect()
    ccs.protect()
    if players:
        for loc,value in enumerate(players):
            if value.death:
                players.pop(loc)
def update_data(dt):
    c1 = time.time()
    check_board(key_board,FALL_key_handler)
    update_mail(dt,key_board)
    protect()
    on_draw()
    
    print( round(time.time() - c1,3),'max:',time_max[0])
    if time.time() - c1 > time_max[0]:
        time_max[0] = time.time() - c1
    print(mouse_trans_1)
    refuse_trans(screen_trans_1)
#check events
game_window.push_handlers(FALL_key_handler)
#game_window.push_handlers(players[1].key_handler)
#game_window.pop_handlers()
pyglet.clock.schedule_interval(update_data, 1/480.0)
##pyglet.clock.schedule_once(self.die, 0.5)
@game_window.event
def on_mouse_motion(x,y,dx,dy):
    mouse_trans_1[0] = x
    mouse_trans_1[1] = y
    mouse_trans_1[2] = dx
    mouse_trans_1[3] = dy
    ammow.x = x
    ammow.y = y
@game_window.event
def on_mouse_press(x,y,dx,dy):
    mouse_trans_1[0] = x
    mouse_trans_1[1] = y
    mouse_trans_1[2] = dx
    mouse_trans_1[3] = dy
    ammow.x = x
    ammow.y = y

if __name__ == '__main__':
    pyglet.clock.schedule_once(zero_time, 0.5)
    pyglet.app.run()


