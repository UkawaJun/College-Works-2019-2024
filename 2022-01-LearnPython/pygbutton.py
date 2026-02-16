import pygame.font
from random import randint
class Button(): 
    def __init__(self, screen, msg): 
        self.screen = screen 
        self.screen_rect = screen.get_rect() 
        
        # 尺寸和其他属性
        self.width, self.height = 200, 50 
        self.msg_back_color = (100, 200, 100) 
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48) 
 
        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height) 
        self.rect.center = self.screen_rect.center 
 
        # 按钮的标签只需创建一次
        self.prep_msg(msg)
    def prep_msg(self, msg): 
    #将msg渲染为图像，并使其在按钮上居中
        self.msg_image = self.font.render(msg, False, self.text_color, self.msg_back_color)    #@surface
        #把文本转为图像：msg    #2 是否开启抗锯齿     
        self.msg_image_rect = self.msg_image.get_rect()     #获取图像的rect
        self.msg_image_rect.center = self.rect.center
    def draw_button(self,x,y,color): 
    # 绘制一个用颜色填充的按钮，再绘制文本
        self.rect = pygame.Rect(0, 0, self.width + 5, self.height + 5)
        self.rect.centerx = x
        self.rect.centery = y
        self.screen.fill(color, self.rect)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = x
        self.rect.centery = y
        self.screen.fill(self.msg_back_color, self.rect) 
        self.msg_image_rect.centerx = x
        self.msg_image_rect.centery = y
        self.screen.blit(self.msg_image,self.msg_image_rect)
class stars():
    def __init__(self, screen,length,wide):
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 2)
        self.rect.centerx = randint(0,length)
        self.rect.centery = randint(0,wide)
        self.color = 255,200,255      
    def draws(self): 
        pygame.draw.rect(self.screen, self.color, self.rect)

def highscoreR():
    filename = 'pyg\score.txt' 
    score = ""
    with open(filename, 'r') as obj:
        score = obj.read()
    list0 = score.split('.')
    return list0
def highscoreW(score):
    filename = 'pyg\score.txt' 
    with open(filename, 'w') as obj:
        obj.write(str(score))







