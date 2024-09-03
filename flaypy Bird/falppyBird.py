import random  #for genrating random numbers
import sys
#we will use sys.exit to exxit the program
import pygame
from pygame.locals import *

#golobal variabel
fps = 32
screen_width = 289
screen_height = 511
screen = pygame.display.set_mode((screen_width,screen_height))
ground = screen_height*0.8
game_sprites={}
game_sound={}
bird = 'bird,png'
background='background.png'
pipe='danda.png'

def welcomeScreen():
    #   birdx=int(screen_width/5)
    # birdy=int((screen_height-game_sprites['bird'].get_height))

    # messagex=int((screen_width - game_sprites['message'].get_width())/2)
    # messagey=int(screen_height*0.13)
   
    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT or ( event.type==KEYDOWN and event.type == K_SPACE):
                pygame.quit()
                sys.exit()
                # pygame.display.update()
                # fpdclock.tick(fps)
            elif  event.type == KEYDOWN and (event.type == K_SPACE or event.type == K_UP):
                return
            else:
                screen.blit(ovimg,(0,0))
                # screen.blit(game_sprites['message'],(0,0))
                # screen.blit(game_sprites['bird'],(birdx,birdy))
                pygame.display.update()
                fpsclock.tick (fps)

#main function jhn sa game start ho hoga 
#main pout
if __name__ == "__main__":
    pygame.init()
    fpsclock = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird by Misbah')
    # game_sprites['number'] =(
    #     pygame.image.load('0.png').convert_alpha(),
    #     pygame.image.load('01.png').convert_alpha(),
    #     pygame.image.load('02.png').convert_alpha(),
    #     pygame.image.load('03.png').convert_alpha(),
    #     pygame.image.load('04.png').convert_alpha(),
    #     pygame.image.load('05.png').convert_alpha(),
    #     pygame.image.load('06.png').convert_alpha(),
    #     pygame.image.load('07.png').convert_alpha(),
    #     pygame.image.load('08.png').convert_alpha(),
    #     pygame.image.load('09.png').convert_alpha(),     
    # )
    # game_sprites['message']=pygame.image.load('message.jpg').convert_alpha()
    ovimg = pygame.image.load("message.png")
    ovimg = pygame.transform.scale(ovimg, (screen_width,screen_height)).convert_alpha()
 

    # game_sprites['pipe']=(
    #     pygame.transform.rotate(pygame.image.load(pipe).convert_alpha(),180),
    #     pygame.image.load(pipe).convert_alpha()
    # )
    # game_sound['die']=pygame.mixer.Sound('die.mp3')
    # game_sound['hit']=pygame.mixer.Sound('hit.mp3')
    # game_sound['point']=pygame.mixer.Sound('point.mp3')
    # game_sound['swoosh']=pygame.mixer.Sound('swoosh.mp3')
    # game_sound['win']=pygame.mixer.Sound('win.mp3')
    
    # game_sprites['background']=pygame.image.load(background).convert()
    # game_sprites['bird']=pygame.image.load(bird).convert_alpha() 

    while True:
        welcomeScreen()