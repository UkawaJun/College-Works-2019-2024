import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
import sys
from time import sleep
from random import randint  #随机数的库

from pygbutton import Button,highscoreR,highscoreW,stars
random_number = randint(-10,10)
import pygame
pygame.mixer.init()
#游戏碰撞敌人的时候，减少子弹的测试有问题
bool_list = [False,False,False]
s_step = 1
speed:float = 0.6
realstep:float = s_step*speed
length:int =1600
wide:int = length / 2


fov = 1
test = False
zhenshu = 1
gromax = 30
#此处正尝试通过字符拼接来捏造地址
class enity(Sprite): 
    def __init__(self, screen,name): 
        super(enity, self).__init__()
        self.screen = screen 
        locapname = 'pyg' + '\\' + str(name)  +'.bmp' #转义字符 即\\的目的是为了让编译器明白：假设换行符的例子
        self.image = pygame.image.load(locapname)        # @surface
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect() 
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom

        self.keep_KDown_left = False
        self.keep_KDown_right = False
        self.keep_KDown_up = False
        self.keep_KDown_down = False

        self.locationx = self.rect.centerx
        self.locationy = self.rect.centery
        self.rectLen = self.rect.right - self.rect.left
        self.rectWid = self.rect.bottom - self.rect.top
        
        self.individual = randint(0,gromax)
        self.ani_shoot = False
    def plane_check(self,real):
        if(self.rect.right == self.screen_rect.right):
            real[1] = -1
            real[0] = True
        elif(self.rect.left == self.screen_rect.left):
            real[1] = 1
            real[0] = True
    def updata(self):       #当目标为可被移动键操作时
        if self.keep_KDown_right:
            self.locationx += realstep
        elif self.keep_KDown_left:
            self.locationx -= realstep
        elif self.keep_KDown_up:
            self.locationy -= realstep
        elif self.keep_KDown_down:
            self.locationy += realstep
    def plane_updata(self,speed:float,realZ):       #飞机大战敌人的AI
        if realZ[0]:
            self.locationy += float(0.5 * speed)
        else:
            self.locationx += float(realZ[1] * speed)
    def plane_shoots(self,groove1,bullets_ani,screen):
        if(self.individual + groove1 > 31) and not self.ani_shoot :
            self.ani_shoot = True
            new_bull = bullets(screen,self)
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            new_bull.color = (r,g,b) 
            bullets_ani.add(new_bull)
    def reset(self):
        self.locationx = self.rect.centerx 
        self.locationy = self.rect.centery 
    def lochange(self,floatx:float,floaty:float):
        self.locationx = floatx
        self.locationy = floaty
    def protect(self):
        if(self.rect.left < self.screen_rect.left):
            self.locationx += realstep
            bool_list[0] = False
        elif(self.rect.right > self.screen_rect.right):
            self.locationx -= realstep
            bool_list[0] = True
        elif(self.rect.top < self.screen_rect.top):
            self.locationy += realstep
            bool_list[1] = False
        elif(self.rect.bottom > self.screen_rect.bottom):
            self.locationy -= realstep
            bool_list[1] = True
        #保护之后更新
        self.rect.centerx = self.locationx
        self.rect.centery = self.locationy

    def protect2(self,sure:bool,defeat = []):
        if(self.rect.left < self.screen_rect.left):
            self.rect.left = self.screen_rect.left
            self.reset()
            bool_list[0] = False
        elif(self.rect.right > self.screen_rect.right):
            self.rect.right = self.screen_rect.right
            self.reset()
            bool_list[0] = True
        elif(self.rect.top < self.screen_rect.top):
            self.rect.top = self.screen_rect.top
            self.reset()
            bool_list[1] = False
        elif(self.rect.bottom > self.screen_rect.bottom):
            if (sure):
                defeat[0] = True
            self.rect.bottom = self.screen_rect.bottom
            self.reset()
            bool_list[1] = True
        #保护之后更新
        self.rect.centerx = self.locationx
        self.rect.centery = self.locationy
    def up_data_screen(self):
        self.screen.blit(self.image, self.rect)

class bullets(Sprite):
    def __init__(self, screen,ship):
        super(bullets, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 20)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.locationy =self.rect.y
        self.color = 255,30,30       #  == (60,60,60)
        self.speed:float = 1
    def update(self): 
        #移动子弹
        self.locationy -= self.speed *2
        self.rect.y = self.locationy
    def update_a(self,aniy_shoot): 
        #移动子弹
        self.locationy += aniy_shoot *1.2
        self.rect.y = self.locationy
    def draws(self): 
        pygame.draw.rect(self.screen, self.color, self.rect)
def check_events(target,target_01,screen,now,game_start,num_OF_bullets_allow):
    #监测鼠标类键盘的动作
    for event in pygame.event.get():        #取得所有的事件 包括按下鼠标按键 按下键盘 移动鼠标
        if event.type == pygame.QUIT:       #get()抓取事件，是队列式的抓取 pop
            sys.exit()
        elif event.type == pygame.KEYDOWN:  #按下
            if event.key ==pygame.K_F1:
                 sys.exit()
            if event.key == pygame.K_s:
                pygame.mouse.set_visible(True)
                game_start[0] = False
            if event.key == pygame.K_SPACE and now[0] <= num_OF_bullets_allow:
                now[0] += 1
                new_bull = bullets(screen,target)
                target_01.add(new_bull)
            if event.key == pygame.K_RIGHT:
                target.keep_KDown_right = True
            elif event.key == pygame.K_LEFT:
                target.keep_KDown_left = True
            elif event.key == pygame.K_UP:
                target.keep_KDown_up = True
            elif event.key == pygame.K_DOWN:
                target.keep_KDown_down = True
        elif event.type == pygame.KEYUP:    #松开
            if event.key == pygame.K_RIGHT:
                target.keep_KDown_right = False
            elif event.key == pygame.K_LEFT:
                target.keep_KDown_left = False
            elif event.key == pygame.K_UP:
                target.keep_KDown_up = False
            elif event.key == pygame.K_DOWN:
                target.keep_KDown_down = False
def creat_ani(ones,OLineAni,distance,screen,animyo,line):
    ones.lochange(45.0,60.0)
    for inti0 in range(0,line):
        for inti in range(0,OLineAni):
            new_one = enity(screen,'A')
            new_one.lochange(ones.locationx + inti * (distance + ones.rectLen),ones.locationy + inti0 * distance)
            animyo.add(new_one)
    ones.lochange(0.0,0.0)  #2初始化一个进度条

    
def main():
    sound = pygame.mixer.Sound("pyg\Intro.mp3")
    sound.set_volume(0.3)
    num_OF_bullets_allow:int = 6
    highscore_list = highscoreR()
    HighScore = str(highscore_list[0])+ '.' + str(highscore_list[1])
    pygame.init()
    screen = pygame.display.set_mode((length, wide))
    ships = Group()
    ship = enity(screen,'PL')
    ships.add(ship)

    ones = enity(screen,'A')
    ones.lochange(45.0,60.0)    #代表纵队的初始位置

    #out create bullets
    bullets0 = Group()      #@ group
    bullets_ani = Group()
    now_bullets = [1]       #表示第一发子弹的当前编号
    animyo =Group()    
    #创造5排根据屏幕长度而变化的
    distance = 80.0
    mathx:int = ones.rectLen + int(distance) 
    OLineAni = (int)((length -45) / mathx)
    line = 5
    aniy_speed = 0.06
    aniy_shoot = 0.3
    aniy_damage = 7
    creat_ani(ones,OLineAni,distance,screen,animyo,line)
    realZ = [False,1]       #1:代表敌人碰壁后允许敌人向下运动的开关 #2代表方向向量

    game_start = [False]
    #button  and score
    but0 = Button(screen,"play")
    score = 0
    score_dra = Button(screen,(str)(score))
    score_dra.msg_back_color = 104,130,128
    score_dra.text_color = (240,220,20)
    
    groove0 = 0.0
    groove1 = 0.0
    groove1_inspeed = 0.005
    levels = 1
    level_dra = Button(screen,(str)(levels))
    level_dra.msg_back_color = 100,10,128
    level_dra.text_color = (255,100,100)
    floor = 10
    ani_down = 35
    exchange = 1.0
    line = 2

    lefl = levels * floor
    defeat = [False]
    star0 = list()
    for num in range(0,500):
        newstar = stars(screen,length,wide)
        star0.append(newstar)
    while True:
        if defeat[0]:
            nowScore = str(levels)+ '.' + str(score)
            pygame.mouse.set_visible(True)
            but1 = Button(screen,"You Lost!!your level is "+ str(levels) + "." + str(score))
            if (levels > int(highscore_list[0])):
                 but2 = Button(screen,"You are High score"+ nowScore)
                 highscoreW(nowScore)
            elif(levels < int(highscore_list[0])):
                 but2 = Button(screen,"and high score is"+ HighScore)
            elif(levels == int(highscore_list[0])):
                 if (score > int(highscore_list[1])):
                     but2 = Button(screen,"You are High score!"+ nowScore)
                     highscoreW(nowScore)
                 elif(score < int(highscore_list[1])):
                     but2 = Button(screen,"and high score is"+ HighScore)
                 elif(score == int(highscore_list[1])):
                     but2 = Button(screen,"twin win!"+ HighScore)
            while True:
                screen.fill((200,120,100))
                for event in pygame.event.get():        
                    if event.type == pygame.QUIT:      
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:  #按下
                        if event.key ==pygame.K_a:
                            main()
                but1.draw_button(800,400,(230,160,160))
                but2.draw_button(800,500,(230,160,160))
                pygame.display.flip() 
        elif not game_start[0]:
            for event in pygame.event.get():        
                if event.type == pygame.QUIT:      
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x,mouse_y = pygame.mouse.get_pos()        #@ back tuple
                    if but0.rect.collidepoint(mouse_x, mouse_y):    #检测该点是否碰撞了该对象的rect
                        print("\a")
                        game_start[0] = True
            screen.fill((100,120,100))
            but0.draw_button(800,400,(230,160,160))
            pygame.display.flip() 
        else:
            sound.play()
            r = (0.5 * groove1) + 10
            g = (0.5 * groove1) + 10
            b = (1.4 * groove1) + 30
            groove1 += groove1_inspeed
            ##score
            if not(animyo):     #意见是已经看见子弹撞击的时候已经执行下一帧
                bullets0.empty()        #@清空元组内的对象
                creat_ani(ones,OLineAni,distance,screen,animyo,line)
            pygame.mouse.set_visible(False)         #隐藏光标
            screen.fill((r,g,b))
            #---#检测步骤
            for ship in ships:
                check_events(ship,bullets0,screen,now_bullets,game_start,num_OF_bullets_allow)
            for a in animyo:   
                a.plane_check(realZ)
        
            #---#更新步骤：把数值变为目标方向
                #表示渲染”上“一帧的已经被显示出来的碰撞   敌人碰撞
            score_dra.msg_image = score_dra.font.render((str)(score), False, score_dra.text_color, score_dra.msg_back_color)
            level_dra.msg_image = level_dra.font.render((str)(lefl) + "%" + (str)(levels), False, level_dra.text_color, level_dra.msg_back_color) 
            coll = pygame.sprite.groupcollide(bullets0, animyo, True, True)
            #                                  group   group    这两选true代表相对位置的会消失
            coll2 = pygame.sprite.groupcollide(bullets_ani,ships, True, False)
            
            if coll:
                #print(coll)
                adscore = 0
                for a in coll.keys():
                    adscore = len(coll[a])
                score += adscore * (int)(exchange)    #@ int
                #input(coll)
                print("\a")     #转义字符蜂鸣
                sleep(0.015)      #
                now_bullets[0] -= 1
            if coll2:
                score -= aniy_damage
            if(realZ[0]):           
                groove0 += aniy_speed
                if(groove0 > ani_down):
                    groove0  = 0.0
                    realZ[0] = False
            for ship in ships:
                ship.updata()
            for bul in bullets0:    #等价#bullets0.update()  更新子弹堆里的所有子弹
                bul.update()
            for bul in bullets_ani:    #等价#bullets0.update()  更新子弹堆里的所有子弹
                bul.update_a(aniy_shoot)
            for ai in animyo:   
                ai.plane_updata(aniy_speed,realZ)
                ai.plane_shoots(groove1,bullets_ani,screen)

            #---#保护步骤 也就是调整数据 并同时把数据定值
            for ship in ships:
                ship.protect2(False)
            for animy in animyo:
                animy.protect2(True,defeat)
                #删除移除屏幕外的子弹
            for bul in bullets0:
                if(bul.rect.bottom <=0):
                    score -= 1
                    now_bullets[0] -= 1
                    bullets0.remove(bul)
            for bul2 in bullets_ani:
                if(bul2.rect.bottom >= 800):
                    bullets_ani.remove(bul2)
            for ship in ships:
                if pygame.sprite.spritecollideany(ship, animyo) or score < -30:
                    defeat[0] = True
            if(groove1 > gromax):
                for ai in animyo:
                    ai.ani_shoot = False
                groove1  = 0.0
            #---#绘制步骤 ： 确保数据，目标全部调整后统一的进行绘制 ：即绘制先后已经无所谓了
            for star in star0:
                star.draws()
            score_dra.draw_button(800,460,(200,200,200))
            level_dra.draw_button(800,400,(200,200,200))
            for bul in bullets0:
                bul.draws()
            for bul in bullets_ani:
                bul.draws() 
            for animy in animyo:
                animy.up_data_screen()
            for ship in ships:
                ship.up_data_screen()
            
            #---#刷新帧
            pygame.display.flip() 
            if(score >= lefl):
                levels += 1
                aniy_damage += 1
                score -= (int)((levels * floor)/2)
                ani_down += 4
                aniy_speed += 0.018
                aniy_shoot += 0.03
                exchange += 0.6
                floor += 2
                groove1_inspeed += 0.0025
                if(levels % 5 == 0) and not (levels == 0):
                    line += 1
                    num_OF_bullets_allow += 2
                lefl = levels * floor
if __name__ == '__main__':        
    main()

