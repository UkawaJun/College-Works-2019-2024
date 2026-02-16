import pyglet,random,math
from pyglet.window import key
from PIL import Image
import numpy as np
rtf = 0.0174532925166   #==pi/180 1度 = rtf*1弧度
#def on_mouse_leave(x, y)
#def on_mouse_enter(x, y)
#def on_mouse_motion(x,y,dx,dy)  移动
#def on_mouse_press(x, y, button, modifiers):
#circle = pyglet.shapes.Circle(x=100, y=150, radius=40, color=(224, 200, 225))
#pattern = pyglet.image.SolidColorImagePattern(color=(200,100,230,255))
#image = pattern.create_image(150,2)
#second = pyglet.sprite.Sprite(image, x=800, y=500)
def PIC_index(file,pixel_table):
    I = Image.open(file) 
    I_array = np.array(I)
    pixel_table[file] =  {'scale':[len(I_array[0]),len(I_array)],'pixel':I_array }
    return pixel_table[file]
def distance(point_1=[0.0,0.0], point_2=[0.0,0.0]):
    """Returns the distance between two points"""
    return math.sqrt((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)
def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2
def refuse_trans(screen_trans):
    screen_trans[0] = 0.0
    screen_trans[1] = 0.0
def check_board(key_board,FALL_key_handler):
    #摘录修改的函数
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
def rotate(point_1 = [0,0],target = [0,0],thus = 90):
    """给一个点 按照第二个点进行旋转"""
    if thus == 0:
        return point_1
    centered = [point_1[0] - target[0],point_1[1] - target[1]]
    angle = line_angle([0,0],centered)
    r = distance(centered)
    if r == 0:
        r = 0.000001
    reathus = (angle + thus)*rtf
    #input( "sss"+ str(reathus) + "sss")
    centered[0] = r * math.cos(reathus)
    centered[1] = r * math.sin(reathus)
    centered = [centered[0] + target[0],centered[1] + target[1]]
    return centered
def dot_for_line(line_point1 = [1,1],line_point2 = [-1,-1],target = [0,0],k=[1],thus = [1.00]):
    #判断三种情况 垂直线
    thus[0] = line_angle(line_point1,line_point2,k) 
    if(thus[0] == 90 or thus[0] == 270):
        if(target[0] == line_point2[0]):
            return '9in'
        elif(target[0] > line_point2[0]):
            return '9big'       #向左为小 向右为大
        else:
            return '9small'
    #y = y1 + x*k - x1*k
    if(thus[0] == 180 or thus[0] == 0):
        k[0] = 0
        if(target[1] == line_point2[1]):
            return 'in'
        elif(target[1] > line_point2[1]):
            return 'big'       #向左为小 向右为大
        else:
            return 'small'
    y1 = line_point1[1]  + k[0]*(target[0] -line_point1[0])
    if(target[1] == y1):
        return 'in'
    elif(target[1] > y1):
        return 'big'
    else:
        return 'small'
def block_in(box = [[1,1],[1,-1],[-1,-1],[-1,1]],taget_point = [0,2],center = [0,0]):
    #是测试自己的四个点 是否在对方的四个点范围之内
    tl = []
    div = 0
    listbs = []
    r = distance(box[0],center)
    r2 = distance(taget_point,center)
    if(r2 > r):
        return False
    str0 = ''
    for a in box:
        listbs.append(a)
    listbs.append(box[0])
    for a  in range(0,4):
        str0 = dot_for_line(listbs[a],listbs[a + 1],taget_point)
        tl.append(str0)
        if (str0 =='big' or str0 =='9big'):
            div += 1
        else:
            div -= 1
    if div == 0:
        return True
    else:
        return False
def line_angle(line_point1 = [1,1],line_point2 = [-1,-1],k = [1]):
    #也是在计算向量角度
    x2_c_x1 = (line_point2[0] - line_point1[0] )
    y2_c_y1 = (line_point2[1] - line_point1[1] )
    x2_than_x1 = (line_point2[0] - line_point1[0] > 0)
    y2_than_y1 = (line_point2[1] - line_point1[1] > 0)
    if(x2_c_x1 == 0):
        if(y2_than_y1):
            return 90;
        else:
            return 270;
    if(y2_c_y1 == 0):
        k[0] = 0
        if(x2_than_x1):
            return 0;
        else:
            return 180;
    k[0] = (y2_c_y1 )/(x2_c_x1)
    #角度
    tan_ok_thus = math.atan(k[0]) / rtf
    if(tan_ok_thus > 0):
        if x2_c_x1 > 0:
            return round(tan_ok_thus,2)
        else:
            return round(tan_ok_thus + 180,2)
    else:
        if x2_c_x1 > 0:
            return round(tan_ok_thus +360 ,2)
        else:
            return round(tan_ok_thus + 180,2)
class Text():
     def __init__(self,content,location = [0.0,0.0]):
         self.content = pyglet.text.Label(text = content, x=location[0], y =location[1],
                                          anchor_x='left',font_size=12,bold=True,color=(0, 0, 0, 255))
         self.content.x = 100
class AI():
    def __init__(self,size = 1):

        size0 = size
        if size0 <0:
            size0 = 1
        
  ######必须存在部分：       #object里的死是彻底意义上的死掉了 不再发生 ias里的死是可以持续生效和作用的    
        #thrust 推力
        self.thrust = 300.0
        #rotate_speed 旋转力
        self.rotate_speed = 200.0
######## 可调整部分：
        #articulo  濒死态
        self.artdeath = False
        #health 生命值
        self.health = 20.0
        #health 护甲值
        self.armor = 20.0
        self.damage = 5
        #状态闭环 是否移动 是否旋转!
        self.is_move = False
        self.last_move = False
        self.is_rota = False
        self.last_rota = False
        #梯队式 队列式水槽？ new_concept 表示可以游离调整的部分

        self.animation = [] 
        self.animation2 = []        #更动画使用的
        #一个单位数据槽为 3  有漏水 和 输水的设定 捏
        #TK: 用于参数储存 一般对应坐标变换(2D) 2足够
        self.data_ibit1 = []
        self.data_ibit2 = []
        self.data_fbit1 = []
        self.data_fbit2 = []
        self.data_channel = []
        for a in range(0,2*size0):
            self.data_ibit1.append(0)
            self.data_ibit2.append(0)
            self.data_fbit1.append(0.0)
            self.data_fbit2.append(0.0)
            #self.data_channel.append(0.0)
            self.data_channel.append(0.0)
    def waltest(self,tar = 50.0,end = 100.0,fov = 1.0):
        wal =  tar/end      # 0 -- 1.0 
        if wal > 1.0 :
            wal = 1.0
        if wal < 0.0:
            wal = 0.0
        return wal*fov
class Object(pyglet.sprite.Sprite):
    def __init__(self,image,in_num = 0,spaces = 1, *args, **kwargs):  #OT
        super(Object, self).__init__(img = image,*args, **kwargs)
        self.bool_list = {'box.open':True,'box.rota':True,'box_setting':False,
                          'is_box_true':False,'is_owner':False}
        
        #表示 是否 自动 更新碰撞箱 和更新旋转碰撞箱
        self.images = []
        # 0位 上的是主索引 是实物的主索引 有关爆炸 等材质信息
        self.images.append(image)
        self.imagei = { 'img': [],'sizeTable' : [],
                       'directTable' : [],'full_size':1,
                       'imgscale':[],'dispose':[],'count':0}
       
        self.image_now = 0
        self.imgwid = self.images[self.image_now].width * self.scale
        self.imghei = self.images[self.image_now].height * self.scale
        self.image_append(image)

        self.velocity_x, self.velocity_y = 0.0, 0.0
        #self.active_x, self.active_y = 0.0, 0.0
        #self.image_setting(1,modle = 'center')
        #碰撞箱点集 正常箱 旋转箱 和 自定义箱子
        self.box = [[self.x ,self.y],[self.x+self.imgwid/2,self.y],
                    [self.x+self.imgwid/2,self.y+self.images[0].height/2],[self.x,self.y + self.images[0].height/2]]
        self.rota_box = [[self.x ,self.y],[self.x+self.imgwid/2,self.y],
                    [self.x+self.imgwid/2,self.y+self.images[0].height/2],[self.x,self.y + self.images[0].height/2]]
        self.box_kind = [self.imgwid,self.imghei]
        self.control = False
        self.text = False
        self.texts = Text('?',location = [0.0,0.0])
        #self.init_location = [self.x,self.y]
        #以x轴为0 向左旋转多少度 为基准方向数值
        self.rota = 0.0
        self.direct = 90.0
        self.tans2 = self.rota + self.direct 

        #ROTA 为初始方向 逆时针为正所旋转的角度 direct为初始朝向 也是逆时针为正
        #即时刻的朝向既 rota + direct
        self.death = False
        self.thrust = 300.0
        self.rotate_speed = 200.0
        ####box-->
        self.is_boxes = [   ]  #碰撞箱生效的内容 均会加入其中！
        self.team = []     #所从属爸爸 被加入团队之后 拥有其团队的地址
        self.father = []   #如武器 被拥有之后 拥有其所有者的地址
        self.number = in_num  # 编号
        self.owner = Team()
        self.owner.s_owner(self)
        #### cauls
        self.ias = AI(spaces)
    def get_tans2(self):
        self.tans2 = self.rota + self.direct 
        if self.tans2 < 0:
            self.tans2 = 360.0 + self.tans2 
        if self.tans2 > 360:
            self.tans2 = self.tans2 - 360.0
        return self.tans2
    def dates_itsself(self,dt,screen_trans=[0.0,0.0]):
        #为仅更新  它的 随从的版本
        self.owner.datas(dt,screen_trans)
    def update(self, dt,screen_trans=[0.0,0.0]): #ET
        #为仅更新自己的版本
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
            #自然秩序为主的更新于终下：
        self.x += screen_trans[0]
        self.y += screen_trans[1]
            #把时间敏感的操作均*t
        self.protect()
    def ObjInang(self,object,k = [0]):
        # return the angle between twice!
        return line_angle([self.x,self.y],[object.x,object.y],k)
    def ObjReloc(self,x,y):
        if (self.x == x and self.y == y):
            return False
        self.x = x
        self.y = y
        self.ias.is_move = True
        return True
    def Obj_rotation(self,thus):  #EO
        if thus == 0:
            return False
        self.rota += thus
        self.rotation = -self.rota
        self.ias.is_rota = True
        return True
    def ObjWatch_object(self,object2,dir = True):
	    # a向着 b 转向
        tans = line_angle([self.x,self.y],[object2.x,object2.y]) 
        if tans == self.get_tans2():
            return False
        if not dir:
            if tans < 180:
                tans += 180
            else:
                tans -= 180
        self.rotation = -tans + self.direct
        self.rota = - self.rotation
        self.ias.is_rota = True
        return True
    def ObjWatch_loc(self,loc = [100.0,200.0],dir = True):
	    # a向着 b 转向
        tans = line_angle([self.x,self.y],loc)
        if tans == self.get_tans2():
            return False
        if not dir:
            if tans < 180:
                tans += 180
            else:
                tans -= 180
        self.rotation = -tans + self.direct
        self.rota = - self.rotation
        self.ias.is_rota = True
        return True
    def ObjWatch_angle(self,angle = 0.0,dir = True):
	    # a向着 b 转向
        tans = angle
        if tans == self.get_tans2():
            return False
        if not dir:
            if tans < 180:
                tans += 180
            else:
                tans -= 180
        self.rotation = -tans + self.direct
        self.rota = - self.rotation
        self.ias.is_rota = True
        return True
    def Objbounce(self,object,dt,pre = 1):

        ###调查  1.判断交给自函数做  2.判断交给调用函数前做  3.减少不必要遍历数目
        if(not(object.ias.last_move or object.ias.last_rota)):
           return False
           pass
        if(self == object):
            return False
        #object 小于 self时候  出bug
        box = []
        box2 = []
        targets = []
        dis1,dis2 = 0.0,0.0
        test = False
        max0 = 0.0
        if self.bool_list['box.rota']:
            box = self.rota_box
        else:
            box = self.box
        if object.bool_list['box.rota']:
            box2 = object.rota_box
        else:
            box2 = object.box
        dis0 = distance([object.x,object.y],[self.x,self.y])
        dis1 = distance(box[0],[self.x,self.y])
        dis2 = distance(box2[0],[object.x,object.y])
        if dis2 > dis1:
            max0 = dis1/2 + dis2
        else:
            max0 = dis1 + dis2/2
        if(dis0 > dis1 + dis2):
            return False
        if dis2 < dis1:
            test = object.boxColli(self)
            if not test:
                test = self.boxColli(object) or test
        else:
            test = self.boxColli(object)
            if not test:
                test = object.boxColli(self) or test
        while test :
            self.ObjFord(object,dt/10,dire = -1,stlen = 0.0)   
            self.data_box()
            if dis2 < dis1:
                test = object.boxColli(self)
                if not test:
                    test = self.boxColli(object) or test
            else:
                test = self.boxColli(object)
                if not test:
                    test = object.boxColli(self) or test
            if test == False:
                self.ias.is_move = True
                test = True
                break;
            #test = object.boxColli(self) or self.boxColli(object)
            # for the easily 为了更有效的运算 既然都已经调用距离函数 不妨就设定更多的界限
        return test
    def ObjFord(self,object2,dt,stlen =40.0,dire=1):
        #a 向着 b 移动
        if distance([self.x,self.y],[object2.x,object2.y]) <= stlen:
            return False
        else:
            tans = line_angle([self.x,self.y],[object2.x,object2.y]) 
            angle_radians = math.radians(tans)
            st = self.ias.thrust * dt
            fov = 0.6
            force_x = math.cos(angle_radians) * st
            force_y = math.sin(angle_radians) * st
            self.x += force_x * fov * dire
            self.y += force_y * fov * dire 
            self.ias.is_move = True
            return True
    def ObjMove_loc(self,dt,loca = [0,0],stlen =40.0,dire=1):
        #a 向着 b坐标 移动
        if distance([self.x,self.y],loca) <= stlen:
            return False
        else:
            tans = line_angle([self.x,self.y],loca) 
            angle_radians = math.radians(tans)
            st = self.ias.thrust * dt 
            fov = 0.6
            force_x = math.cos(angle_radians) * st
            force_y = math.sin(angle_radians) * st
            self.x += force_x * fov * dire
            self.y += force_y * fov * dire 
        self.ias.is_move = True
        return True
    def ObjMove_angle(self,dt,angle = 0,dire=1):
        #a 向着 b angle 移动
        tans = angle
        angle_radians = math.radians(tans)
        st = self.thrust * dt
        fov = 0.6
        force_x = math.cos(angle_radians) * st
        force_y = math.sin(angle_radians) * st
        self.x += force_x * fov * dire
        self.y += force_y * fov * dire 
        self.ias.is_move = True
        return True
    def ObjRota(self,object2,dt,dire=1):
        #a 绕着 b  转向移动
        if True:
            tans = line_angle([self.x,self.y],[object2.x,object2.y]) 
            angle_radians = math.radians(tans + dire*90)
            st = self.thrust * dt
            fov = 0.6
            force_x = math.cos(angle_radians) * st
            force_y = math.sin(angle_radians) * st
            self.x += force_x * fov * dire
            self.y += force_y * fov * dire
            self.ias.move = True
    def ObjTurn_object(self,object2,dt,wave = 0,dir = True):
	    # a向着 b转向
        direct = 1   #1 为逆时针  0为顺时针
        speed = self.ias.rotate_speed    #1s = 300d
        realspeed = speed/(1/dt) 
        tans = line_angle([self.x,self.y],[object2.x,object2.y]) 
        tans2 =  self.get_tans2()
        if not dir:
            if tans < 180:
                tans += 180
            else:
                tans -= 180
        angle = tans - tans2
        if (math.fabs(angle) < wave + realspeed*2):
            return False
        if angle > 360.0:
            angle = angle - 360.0
        elif angle <0.0:
            angle = 360.0 + angle
        #print(angle)
        if angle > 0.0:
            if angle >180.0:
                direct = 0
            else:
                direct = 1
        else:
            if math.fabs(angle) >180.0:
                direct = 1
            else:
                direct = 0
        #realspeed = speed/(1/dt) 
        #realspeed = 0
        #print(math.fabs(angle))
        if True:
            if direct == 1:
                self.rota += realspeed
                self.rotation -= realspeed
            else:
                self.rota -= realspeed
                self.rotation += realspeed
        self.ias.is_rota = True
        return True
    def ObjTurn_Angle(self,dt,angles,wave = 0,dir = True):
	    # a向着 b转向
        direct = 1   #1 为逆时针  0为顺时针
        speed = self.ias.rotate_speed    #1s = 300d
        tans = angles
        tans2 =  self.get_tans2()
        if not dir:
            if tans < 180:
                tans += 180
            else:
                tans -= 180
        angle = tans - tans2
        if angle > 360.0:
            angle = angle - 360.0
        elif angle <0.0:
            angle = 360.0 + angle
        #print(angle)
        if angle > 0.0:
            if angle >180.0:
                direct = 0
            else:
                direct = 1
        else:
            if math.fabs(angle) >180.0:
                direct = 1
            else:
                direct = 0
        realspeed = speed/(1/dt) 
        #realspeed = 0
        #print(math.fabs(angle))
        if (math.fabs(angle) < wave + realspeed*2):
            return False
        else:
            if direct == 1:
                self.rota += realspeed
                self.rotation -= realspeed
            else:
                self.rota -= realspeed
                self.rotation += realspeed
        self.ias.rota = True
        return True
    def ObjTurn_loc(self,dt,loca = [0,0],wave = 0,dir = True):
	    # a向着 b转向
        direct = 1   #1 为逆时针  0为顺时针
        speed = self.ias.rotate_speed    #1s = 300d
        tans = line_angle([self.x,self.y],loca) 
        tans2 = self.get_tans2()
        if not dir:
            if tans < 180:
                tans += 180
            else:
                tans -= 180
        angle = tans - tans2
        if angle > 360.0:
            angle = angle - 360.0
        elif angle <0.0:
            angle = 360.0 + angle
        #print(angle)
        if angle > 0.0:
            if angle >180.0:
                direct = 0
            else:
                direct = 1
        else:
            if math.fabs(angle) >180.0:
                direct = 1
            else:
                direct = 0
        realspeed = speed/(1/dt) 
        #realspeed = 0
        #print(math.fabs(angle))
        if (math.fabs(angle) < wave + realspeed*2):
            return False
        else:
            if direct == 1:
                self.rota += realspeed
                self.rotation -= realspeed
            else:
                self.rota -= realspeed
                self.rotation += realspeed
        self.ias.rota = True
        return True
    def objectReplace(self,weapen):    #team
        if weapen.team:
            for aa in weapen.team:
                if aa.father:
                    aa.father[0] = self
                else:
                    aa.father.append(self)
        self.owner = weapen
        self.owner.number = len(weapen.team)
    def objectCreate(self,weapen:object):
        self.bool_list['is_owner'] = True
        if weapen.father:
            weapen.father[0] = self
        else:
            weapen.father.append(self)
        self.owner.app_object([weapen])
    def objectCreates(self,weapen:list): #传递一组object
        self.bool_list['is_owner'] = True
        for wea in weapen:
            if wea.father:
                wea.father[0] = self
            else:
                wea.father.append(self)
        self.owner.app_object(weapen)
    def image_setting(self,size,modle = 'center',direct = 90.0):  #EO
        if(modle == 'ld'):
            self.images[0].anchor_x = 0
            self.images[0].anchor_y = 0
        elif(modle == 'lu'):
            self.images[0].anchor_x = 0
            self.images[0].anchor_y = self.images[0].height
        elif(modle == 'rd'):
            self.images[0].anchor_x = self.images[0].width
            self.images[0].anchor_y = 0
        elif(modle == 'ru'):
            self.images[0].anchor_x = self.images[0].width
            self.images[0].anchor_y = self.images[0].height
        else:       #中心对齐
            self.images[0].anchor_x = self.images[0].width/2
            self.images[0].anchor_y = self.images[0].height/2
        #设置方向
        self.direct = direct
        self.scale = size
        self.imgwid = self.images[0].width *self.scale
        self.imghei = self.images[0].height *self.scale 
    def image_create(self,modle = 'cri',color=(200,100,230),size = [50,50]):   
        #pattern = pyglet.image.SolidColorImagePattern(color=(200,100,230,255))
        #image = pattern.create_image(150,2)
        #second = pyglet.sprite.Sprite(image, x=800, y=500)
        pattern = pyglet.image.SolidColorImagePattern(color=(200,100,230,255))
        images = pattern.create_image(size[0],size[1])
        second = pyglet.sprite.Sprite(images, x=800, y=500)
        self.image_append(second.image)
        return second.image
    def image_append(self,image,size_ = 1,direct_ = 90.0,modle = 'center'):
        #self.imagei = { 'img': [],'sizeTable' : [],
        #               'directTable' : [],'full_size':1,
        #               'imgscale':[],'count':0}
        if image in  self.imagei['img']:
            return False
        if(modle == 'ld'):
            image.anchor_x = 0
            image.anchor_y = 0
        elif(modle == 'lu'):
            image.anchor_x = 0
            image.anchor_y = image.height
        elif(modle == 'rd'):
            image.anchor_x = image.width
            image.anchor_y = 0
        elif(modle == 'ru'):
            image.anchor_x = image.width
            image.anchor_y = image.height
        else:       #中心对齐
            image.anchor_x = image.width/2
            image.anchor_y = image.height/2
        self.imagei['img'].append(image)
        self.imagei['sizeTable'].append(size_)
        self.imagei['directTable'].append(direct_)
        self.imagei['imgscale'].append([image.width,image.height])    
        self.imagei['count'] += 1
        #self.image = (self.imagei['img'])[self.image_now]
        #self.image = (self.imagei['imgscale'])[self.image_now]   
        return True              
    def image_change(self,loc = 0): 
        #对 loc位 的图像进行参数 ，旋转 和方向 的修改
        #随之而来的包括对碰撞箱的修改和调整
        if loc + 1 > self.imagei['count']:
            loc = self.imagei['count'] - 1
        self.image_now = loc
        self.image = (self.imagei['img'])[loc]   
        #对 loc位 的图像进行参数 ，旋转 和方向 的修改
        self.scale = (self.imagei['sizeTable'])[self.image_now]* (self.imagei['full_size'])
    def image_next(self,step = 1): 
        if step <= 0:
            step = 1
        nloc =(self.image_now + step )%self.imagei['count']
        self.image_now = nloc
        self.image = (self.imagei['img'])[nloc]
        #随之而来的包括对碰撞箱的修改和调整
        #即 位置的修改等
        self.scale = (self.imagei['sizeTable'])[self.image_now]* (self.imagei['full_size'])
    def image_oad(self,size_ = 1,rotas = 0.0,direc = 0.0,full_size = 0):
        #增加
        self.imagei['full_size'] += full_size
        (self.imagei['sizeTable'])[self.image_now] += size_
        self.scale = (self.imagei['sizeTable'])[self.image_now]* (self.imagei['full_size'])
        self.rota += rotas
        self.rotation -= -rotas
        self.direct += direc
        if self.direct > 360:
            self.direct = self.direct - 360.0
    def image_set(self,size_ = 1,full_size = 1):
        #设定 第一个直接设定 第二个 乘法设定
        self.imagei['full_size'] = full_size * self.imagei['full_size']
        (self.imagei['sizeTable'])[self.image_now] = size_
        self.scale = (self.imagei['sizeTable'])[self.image_now]* (self.imagei['full_size'])
    def data_box(self,on = True):   #EO or ET
        #(self.imagei['sizeTable'])[self.image_now] * ((self.imagei['imgscale'])[self.image_now])[0] * (self.imagei['full_size'])
        #(self.imagei['sizeTable'])[self.image_now] * ((self.imagei['imgscale'])[self.image_now])[1] * (self.imagei['full_size'])
        wd = 0.0
        hg = 0.0
        #更新碰撞箱 既 贴图大小改变 旋转 位移时 就进行改变
        if self.bool_list['box_setting']:     
            wd = self.box_kind[0] *(self.imagei['sizeTable'])[self.image_now] * (self.imagei['full_size'])/2
            hg = self.box_kind[1] *(self.imagei['sizeTable'])[self.image_now] * (self.imagei['full_size'])/2
        else: 
            #wd = self.imgwid /2
            #hg = self.imghei /2
            wd = (self.imagei['sizeTable'])[self.image_now] * ((self.imagei['imgscale'])[self.image_now])[0] * (self.imagei['full_size'])/2
            hg = (self.imagei['sizeTable'])[self.image_now] * ((self.imagei['imgscale'])[self.image_now])[1] * (self.imagei['full_size'])/2

        self.box[0] = [self.x +wd,self.y+hg];   self.box[1] = [self.x +wd,self.y-hg];
        self.box[2] = [self.x -wd,self.y-hg];   self.box[3] = [self.x -wd,self.y+hg];
        if self.bool_list['box.rota']:
            self.rota_box[0] = rotate(self.box[0],[self.x,self.y],self.rota)
            self.rota_box[1] = rotate(self.box[1],[self.x,self.y],self.rota)
            self.rota_box[2] = rotate(self.box[2],[self.x,self.y],self.rota)
            self.rota_box[3] = rotate(self.box[3],[self.x,self.y],self.rota)
        else:
            self.rota_box[0] = self.box[0]
            self.rota_box[1] = self.box[1]
            self.rota_box[2] = self.box[2]
            self.rota_box[3] = self.box[3]
    def boxSetCus(self,width,height):     #主动设置碰撞箱
        self.bool_list['box_setting'] = True
        self.box_kind[0] = width
        self.box_kind[1] = height
    def boxColli(self,object):  #检测碰撞！
        box = []
        box2 = []
        if self.bool_list['box.rota']:
            box = self.rota_box
        else:
            box = self.box
        if object.bool_list['box.rota']:
            box2 = object.rota_box
        else:
            box2 = object.box
        #one question  是自己碰到对方 还是对方碰到自己
        str = False
        for me in box:
           str = block_in(box2,me,center = [object.x,object.y])
           if str:
               if object in self.is_boxes:
                   self.bool_list['is_box_true'] = True
                   return True
               else:
                   self.bool_list['is_box_true'] = True
                   self.is_boxes.append(object)
                   return True    
        return False
    def image_setting(self,size,modle = 'center',direct = 90.0):  #EO
        if(modle == 'ld'):
            self.images[0].anchor_x = 0
            self.images[0].anchor_y = 0
        elif(modle == 'lu'):
            self.images[0].anchor_x = 0
            self.images[0].anchor_y = self.images[0].height
        elif(modle == 'rd'):
            self.images[0].anchor_x = self.images[0].width
            self.images[0].anchor_y = 0
        elif(modle == 'ru'):
            self.images[0].anchor_x = self.images[0].width
            self.images[0].anchor_y = self.images[0].height
        else:
            self.images[0].anchor_x = self.images[0].width/2
            self.images[0].anchor_y = self.images[0].height/2
        self.direct = direct
        self.scale = size
        self.imgwid = self.images[0].width *self.scale
        self.imghei = self.images[0].height *self.scale
    def create_talk(self,content,devit = [0.0,0.0]):    #EO
        x0 = devit[0] + self.x
        y0 = devit[1]+ self.y
        self.texts = Text(content = content,location = [x0,y0])
    def protect(self):      #ET
        if self.rota < 0:
            self.rota = 360.0 + self.rota 
        if self.rota > 360:
            self.rota = self.rota - 360.0
        
        if self.bool_list['box.open']:
            self.data_box() 
        self.AI_stateClear()
    def AI_stateClear(self):
        self.ias.last_rota = self.ias.is_rota
        self.ias.last_move = self.ias.is_move
        self.ias.is_move = False
        self.ias.is_rota = False
    def check_bounds(self):         #EO
        min_x = -self.image.width*2
        min_y = -self.image.height*2
        max_x = 1600 + self.image.width*2
        max_y = 1000 + self.image.height*2
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y
class Player(Object):       #即有键盘性操作的目标 也即中心性的 主角
    def __init__(self, *args, **kwargs):    #OT
        super(Player, self).__init__(*args, **kwargs) 
        self.bool0 = True
        self.bool1 = True
    def updates_old(self, dt,key_board,screen_trans=[0.0,0.0]):     #ET
        speed = self.rotate_speed * dt
        st = self.thrust * dt
        force_x = 0.0
        force_y = 0.0
        
        if key_board['a']:
            self.rota += speed
            self.rotation -= speed
        if key_board['d']:
            self.rota -= speed
            self.rotation += speed
        if key_board['w']:
            angle_radians = -math.radians(self.rotation - self.direct)  #正方向定义不同，加负号
            force_x = math.cos(angle_radians) * st
            force_y = math.sin(angle_radians) * st

            screen_trans[0] = -force_x
            screen_trans[1] = -force_y
            #self.x += force_x
            #self.y += force_y
        if key_board['s']:
            angle_radians = -math.radians(self.rotation - self.direct)  #正方向定义不同，加负号
            force_x = math.cos(angle_radians) * st
            force_y = math.sin(angle_radians) * st
            #self.x -= force_x
            #self.y -= force_y
            screen_trans[0] = force_x
            screen_trans[1] = force_y
            #velocity_y
        if key_board['j']:
            self.image_setting(self.scale+1)
            self.o_rotation(1)            
            self.bool_list['box_setting'] = False

        if key_board['t']:
            self.death = True
        super(Player, self).update(dt,[0.0,0.0])    
    def updates_3(self, dt,key_board,screen_trans=[0.0,0.0],mouse = [0,0,0,0]):     #ET
        #ET  顺应鼠标方向移动 图像旋转 当视角在下 左依然向左

        tans = line_angle([self.x,self.y],[mouse[0],mouse[1]]) 
        self.rotation = -tans + self.direct
        #print(round(self.rotation),-tans )
        self.rota = - self.rotation
        #tans是鼠标指向的角度 ：笛卡尔坐标
        angle_radians = math.radians(tans)
        speed = self.rotate_speed * dt
        st = self.thrust * dt
        force_x = 0.0
        force_y = 0.0
        fov = 1.0
        if key_board['w']:
             #正方向定义不同，加负号
            fov = 0.6
            force_x = math.cos(angle_radians) * st
            force_y = math.sin(angle_radians) * st
            screen_trans[0] += -force_x
            screen_trans[1] += -force_y
        if key_board['s']:
            fov = 0.6
            force_x = math.cos(angle_radians) * st
            force_y = math.sin(angle_radians) * st
            screen_trans[0] += force_x
            screen_trans[1] += force_y
        if key_board['a']:
            force_x = math.cos(math.radians((tans +90))) * st
            force_y = math.sin(math.radians((tans +90))) * st
            screen_trans[0] += -force_x * fov
            screen_trans[1] += -force_y * fov
        if key_board['d']:
            force_x = math.cos(math.radians((tans -90))) * st
            force_y = math.sin(math.radians((tans -90))) * st
            screen_trans[0] += -force_x * fov
            screen_trans[1] += -force_y * fov
        self.checks(dt,key_board,screen_trans,mouse)
        
        super(Player, self).update(dt,[0.0,0.0]) 
    def checks(self, dt,key_board,screen_trans=[0.0,0.0],mouse = [0,0,0,0]):
        if key_board['t']:
           # self.death = True
           if self.bool1:
               self.image_next(1)
               self.bool1 = False
        else:
            self.bool1 = True
        if key_board['j']:
            #self.image_setting(self.scale+1)
            if self.bool0:
                self.image_oad(1)      
            self.bool0 = False
            #self.bool_list['box_setting'] = False
        else:
            self.bool0 = True
    def updates_2(self, dt,key_board,screen_trans=[0.0,0.0],mouse = [0,0,0,0]):     #ET
        #ET  顺应鼠标方向移动 图像旋转 当视角在下 左依然向左

        tans = line_angle([self.x,self.y],[mouse[0],mouse[1]]) 
        self.rotation = -tans + self.direct
        self.rota = - self.rotation
        print(tans)
        angle_radians = math.radians(tans)
        speed = self.rotate_speed * dt
        st = self.thrust * dt
        force_x = 0.0
        force_y = 0.0
        fov = 1.0
        if key_board['w']:
              #正方向定义不同，加负号
            fov = 0.6
            force_x = math.cos(angle_radians) * st
            force_y = math.sin(angle_radians) * st

            screen_trans[0] += -force_x
            screen_trans[1] += -force_y
        if key_board['s']:
            fov = 0.6
            force_x = math.cos(angle_radians) * st
            force_y = math.sin(angle_radians) * st

            screen_trans[0] += force_x
            screen_trans[1] += force_y
        if key_board['a']:
            ang = 90.0
            if tans > 180.0 or (tans < 0.0 and tans >= -90.0) :
                ang = -90.0
            force_x = math.cos(math.radians((tans +ang))) * st
            force_y = math.sin(math.radians((tans +ang))) * st

            screen_trans[0] += -force_x * fov
            screen_trans[1] += -force_y * fov
        if key_board['d']:
            ang = 90.0
            if tans > 180.0 or (tans < 0.0 and tans >= -90.0):
                ang = -90.0
            force_x = math.cos(math.radians((tans -ang))) * st
            force_y = math.sin(math.radians((tans -ang))) * st

            screen_trans[0] += -force_x * fov
            screen_trans[1] += -force_y * fov
        
        self.checks(dt,key_board,screen_trans,mouse)
        super(Player, self).update(dt,[0.0,0.0])  
    def updates_1(self, dt,key_board,screen_trans=[0.0,0.0],mouse = [0,0,0,0]):     
        #ET  wsad移动 图像旋转 
        tans = line_angle([self.x,self.y],[mouse[0],mouse[1]]) 
        self.rotation = -tans + self.direct
        self.rota = - self.rotation
        angle_radians = math.radians(tans)
        speed = self.rotate_speed * dt
        st = self.thrust * dt
        force_x = 0.0
        force_y = 0.0
        if key_board['a']:
            force_x += st
        if key_board['d']:
            force_x -= st
        if key_board['w']:
            force_y -= st
        if key_board['s']:
            force_y += st
        screen_trans[0] = force_x
        screen_trans[1] = force_y

        self.checks(dt,key_board,screen_trans,mouse)
        super(Player, self).update(dt,[0.0,0.0]) 
    def updates_4(self,dt):
        super(Player, self).update(dt,[0.0,0.0]) 
        pass
    def Move_it(self,mouse, dt,key_board,screen_trans=[0.0,0.0]):
        #self.ObjTurn_object(mouse,dt*4,wave = 0)
        self.ObjWatch_object(mouse)
        st = self.thrust * dt
        force_x = 0.0
        force_y = 0.0
        
        if key_board['a']:
            force_x += st
        if key_board['d']:
            force_x -= st
        if key_board['w']:
            force_y -= st
        if key_board['s']:
            force_y += st
        screen_trans[0] = force_x
        screen_trans[1] = force_y
        self.checks(dt,key_board,screen_trans,mouse)
        if force_x == 0 and force_y == 0:
            self.ias.is_move = False
        else:
            self.ias.is_move = True
    def delete(self):
        #     ! !  现状不许有任何的删除性行为  ! !     #
        super(Player, self).delete()        
class Team():
    def __init__(self):
        #team 的
        #一个生产子弹的人 会在自己死掉的时候 可以选择性删除自己的子嗣
        #team 更像是ai组 内置对ai的各种调控 同时
        #
        #bool表
        self.bool_list = {'is_be_create': False,'is_twins': False}
        #是否有主人   是否随主人之死而停止行为
        self.team = []      #@转载着object
        self.me = []        #@当object 使用 father 时 会将主人的地址添加于此
        self.number = 0     #@拥有的实体个数 而非存活个数
        self.nlive  = 0     #@存活个数
        # 编号 编队
        self.sign = 'The Adventure'
    def s_owner(self,owner):
        if self.me:
            self.me[0] = owner
        else:
            self.me.append(owner)
        self.bool_list['is_be_create'] = True
    def k_owner(self):
        if self.bool_list['is_be_create']:
            self.bool_list['is_be_create'] = False
            self.me.pop()
    def app_object(self,objects = []):
        #在一个组内部添加成员
        if objects:
            for a in objects:
                if a.team:
                    a.team[0] = self
                else:
                    a.team.append(self)
                self.team.append(a)
        self.number += len(objects)
    def draws(self,centers = [800.0,500.0],leng = 1000.0,index = [0,-1]):
        #默认为屏幕中心为原点的范围内900进行渲染
        c = 0
        if self.team:
            for a in self.team[index[0]:index[1]]:
                if distance(centers,[a.x,a.y]) <= leng:
                    if not a.death:
                        c+=1
                        a.draw()
    def datas(self,dt,screen_trans_1 = [0.0,0.0]):
        #指在此处更新屏幕，如变换 -- 以及在所有变化之后的 所有自然客观因素事物 先是主观动态 后是自然动态
        if self.team:
            for a in self.team:
                if not a.death:
                    a.update(dt,screen_trans_1)
    def team_collEach(self,player,dt):
        for a in self.team:
            a.Objbounce(player,dt)
            if((a.ias.last_move or a.ias.last_rota)):
                for b in self.team:
                    b.Objbounce(a,dt)

    def box_collis(self,target):
        colli = False
        if self.team and target.team:
            for a in self.team:
                for b in target:
                    c = a.boxColli(b)
                    if c == True:
                        colli = True
    #########################################################
    #改动 把删除改成调整 不可以轻易言说事物的死亡！
    def protect(self):
        #请在互相使用之后再调用这个   --各项收尾
        deaths = 0
        
        if self.team:
            if self.bool_list['is_be_create']:        
                if self.me[0].death and self.number != 0:
                    if self.bool_list['is_twins']:
                        for a in self.team:
                            a.death = True    
                            deaths = self.number
            else:
                for a,b in enumerate(self.team):
                    if(b.death):
                        deaths += 1
        self.number = len(self.team)
        self.nlive = self.number - deaths
    
    def dled_protect(self):
        #该保护可以清除 死者数据：无法恢复!
        death_list = []
        if self.team:
            for a,b in enumerate(self.team):
                if(b.death):
                    death_list = self.team.pop(a)
        self.protect()  
        return death_list
    
    ###########################################################
#探测自己是否与一个obj触碰 前提只有自己移动或对方移动才有必要 所以
        #既然以自己为出发点 那就不能时刻把程序视作自己为中心的
        #设定为对方若未移动则不更新盒子@
        #任务清单
        #   1.所有移动 旋转的时候均设置为 True        





