import sys 
import pygame 
import math

screen_color  = (230,230,230)
s_step = 1
speed = 1.4
realstep = float(s_step*speed)
bool_list = [False,False,False]
angle = 0.0000
radi = 3.1415926 / 180.0


def sunset(color,angle):
    angle += 0.0002
    if angle >= 360.0:
       angle = 0.0
    list0 = list(color)
    list0[0] = 230 * math.sin(angle)
    list0[2] = 230 * math.sin(angle)
    return tuple(list0)



class Ship(): 
    def __init__(self, screen): 
        #初始化飞船并设置其初始位置
        self.screen = screen 
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('pyg\happy.gif')        #@surface
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #@rect
        # 将目标的@rect初始化
        self.rect.centerx = self.screen_rect.centerx  -500  #x 
        self.rect.bottom = self.screen_rect.bottom  - 100   #y

        #self.rect.center = self.screen_rect.center
        # #rect     #0，0表示屏幕的左上角 ,而 （length，wide）表示最右下
        #   .centerx表示 @rect 中心的 x坐标 .centery  
        #   .bottom 表示 @rect 最底部的y坐标     .top  表示最顶端的y坐标
        #   .left  表示最左边的x坐标     .right 最右边的x坐标
        #
        self.keep_KDown_left = False
        self.keep_KDown_right = False
        self.keep_KDown_up = False
        self.keep_KDown_down = False

        self.locationx = float(self.rect.centerx)
        self.locationy = float(self.rect.centery)

        self.long = self.rect.centerx - self.rect.left 
        self.short = self.rect.bottom - self.rect.centery
    def blitme(self): 
        #在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)
    def updata(self):
        
        if self.keep_KDown_right:
            self.locationx += realstep
        elif self.keep_KDown_left:
            self.locationx -= realstep
        elif self.keep_KDown_up:
            self.locationy -= realstep
        elif self.keep_KDown_down:
            self.locationy += realstep
    
        self.rect.centerx = self.locationx
        self.rect.centery = self.locationy

       

length =1600
wide = length / 2
def check_events(target):
    #监测鼠标类键盘的动作
    for event in pygame.event.get():        #取得所有的事件 包括按下鼠标按键 按下键盘 移动鼠标
        if event.type == pygame.QUIT: 
            sys.exit() 
        elif event.type == pygame.KEYDOWN:  #按下
            if event.key == pygame.K_RIGHT:
                target.keep_KDown_right = True
                #target.rect.right += s_step
            elif event.key == pygame.K_LEFT:
                target.keep_KDown_left = True
                #target.rect.left -=  s_step
            elif event.key == pygame.K_UP:
                target.keep_KDown_up = True
                #target.rect.top -= s_step
            elif event.key == pygame.K_DOWN:
                target.keep_KDown_down = True
                #target.rect.bottom += s_step
        elif event.type == pygame.KEYUP:    #松开
            if event.key == pygame.K_RIGHT:
                target.keep_KDown_right = False
                #target.rect.right += s_step
            elif event.key == pygame.K_LEFT:
                target.keep_KDown_left = False
                #target.rect.left -=  s_step
            elif event.key == pygame.K_UP:
                target.keep_KDown_up = False
                #target.rect.top -= s_step
            elif event.key == pygame.K_DOWN:
                target.keep_KDown_down = False
                #target.rect.bottom += s_step
def protect(target):
    
    if(target.rect.left < target.screen_rect.left):
        target.locationx += realstep
        bool_list[0] = False
    elif(target.rect.right > target.screen_rect.right):
        target.locationx -= realstep
        bool_list[0] = True
    elif(target.rect.top < target.screen_rect.top):
        target.locationy += realstep
        bool_list[1] = False
    elif(target.rect.bottom > target.screen_rect.bottom):
        target.locationy -= realstep
        bool_list[1] = True
 
    target.rect.centerx = target.locationx
    target.rect.centery = target.locationy

def box(target):
    target.locationx = target.rect.centerx 
    target.locationy = target.rect.centery 

def protect2(target):
    
    if(target.rect.left < target.screen_rect.left):
        target.rect.left = target.screen_rect.left
        box(target)
        bool_list[0] = False
    elif(target.rect.right > target.screen_rect.right):
        target.rect.right = target.screen_rect.right
        box(target)
        bool_list[0] = True
    elif(target.rect.top < target.screen_rect.top):
        target.rect.top = target.screen_rect.top
        box(target)
        bool_list[1] = False
    elif(target.rect.bottom > target.screen_rect.bottom):
        target.rect.bottom = target.screen_rect.bottom
        box(target)
        bool_list[1] = True

    #warning
   


    #一直向左有问题

def main_game(): 
 # 初始化游戏并创建一个屏幕对象
    pygame.init()           #初始化屏幕背景设置
    screen = pygame.display.set_mode((length, wide))  #@screen 
    
    pygame.display.set_caption("Alien Invasion") 
    
    screen.fill(screen_color)
    ship0 = Ship(screen)
# 开始游戏的主循环
    while True: 
 # 让最近绘制的屏幕可见
        check_events(ship0)      #新界面已经绘制了但未更新

        ship0.updata()
        protect(ship0)
        screen.fill(screen_color)
        ship0.blitme()           #新界面已经绘制了但未更新

        pygame.display.flip()   #擦除旧屏幕  更新屏幕


main_game()