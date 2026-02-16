
import pygame

pygame.init()
screen = pygame.display.set_mode((1600, 800))  #@screen 
pygame.display.set_caption("Alien Invasion") 
screen2 = pygame.display.set_mode((500, 800))
pygame.display.set_caption("A22lien Invasion") 

while True:
    for event in pygame.event.get():        #取得所有的事件 包括按下鼠标按键 按下键盘 移动鼠标
        if event.type == pygame.QUIT: 
            sys.exit() 

    pygame.display.flip() 














