import pygame

pygame.mixer.init()
sound = pygame.mixer.Sound("pyg/In.mp3") #@ mp3
sound2 = pygame.mixer.Sound("pyg/Mon.mp3")
while True:
    sound.play()
