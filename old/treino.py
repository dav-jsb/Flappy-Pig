import pygame
from pygame.locals import *
import sys

pygame.init()

x_tela = 700
y_tela = 800

tela = pygame.display.set_mode((x_tela, y_tela))
framerate = pygame.time.Clock()

pos_x = 150
pos_y = 200

velocidade = 0

aceleracao = 2

while True:
    framerate.tick(60)
    
    
    if velocidade >= 5:
        velocidade = 5

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                velocidade -= 35
    
    if velocidade <= -25:
        velocidade = -25
    
    velocidade += aceleracao
    
    pos_y += velocidade

    if pos_y >= y_tela:
        pos_y = 0

    pos_y += 5
    tela.fill((0, 0, 0))

    pygame.draw.circle(tela, (0, 255, 0), (pos_x, pos_y), 15)
    pygame.display.update()
