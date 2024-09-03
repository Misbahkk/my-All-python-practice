from lib2to3.pytree import convert
from turtle import bgcolor
import pygame

pygame.init()

bgimg = pygame.image.load('snake.jpg')
bgimg = pygame.transform.scale(bgimg ,(300,400)).convert_alpha()

window=pygame.display.set_mode((300,400))
window.fill((233,233,233))
window.blit(bgimg,(0,0))
pygame.display.set_caption("Flaypy Bird")
pygame.display.update()
clock = pygame.time.Clock()
game_exit = False


while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit= True
            pygame.display.update()
            clock.tick(60)

pygame.quit()
quit()