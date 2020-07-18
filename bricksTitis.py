import pygame, os, sys
import random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
mainSurface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bricks")

black = pygame.Color(0, 0, 0)

#bat init

bat = pygame.image.load("bat.png")
playerY = 540
batRect = bat.get_rect()
mousex, mousey = (0,playerY)

#ball init
ball = pygame.image.load('ball.png')
ballRect = ball.get_rect()
ballStartY = 250
ballSpeed = 6
ballServed = False
bx, by = (24, ballStartY)
sx, sy = (ballSpeed, ballSpeed)
ballRect.topleft = (bx, by)
#brick init
orden = [0,1,2,3,4,5,6]
random.shuffle(orden)
paula = pygame.image.load('paula.png')
paulas = []
paulaY = (orden[1]*45)+55
for x in range(10):
    paulaX = (x * 38) + 240
    paula_width = paula.get_width()
    paula_height = paula.get_height()
    paula_rect = Rect(paulaX, paulaY, paula_width, paula_height)
    paulas.append(paula_rect)
daniel = pygame.image.load('daniel.png')
daniels = []
danielY = (orden[2]*45)+55
for x in range(10):
    danielX = (x * 38) + 240
    daniel_width = daniel.get_width()
    daniel_height = daniel.get_height()
    daniel_rect = Rect(danielX, danielY, daniel_width, daniel_height)
    daniels.append(daniel_rect)
mili = pygame.image.load('mili.png')
milis = []
miliY = (orden[0]*45)+55
for x in range(10):
    miliX = (x * 38) + 240
    mili_width = mili.get_width()
    mili_height = mili.get_height()
    mili_rect = Rect(miliX, miliY, mili_width, mili_height)
    milis.append(mili_rect)
car = pygame.image.load('car.png')
cars = []
carY = (orden[3]*45)+55
for x in range(10):
    carX = (x * 38) + 240
    car_width = car.get_width()
    car_height = car.get_height()
    car_rect = Rect(carX, carY, car_width, car_height)
    cars.append(car_rect)
maria = pygame.image.load('maria.png')
marias = []
mariaY = (orden[4]*45)+55
for x in range(10):
    mariaX = (x * 38) + 240
    maria_width = maria.get_width()
    maria_height = maria.get_height()
    maria_rect = Rect(mariaX, mariaY, maria_width, maria_height)
    marias.append(maria_rect)
pame = pygame.image.load('pame.png')
pames = []
pameY = (orden[5]*45)+55
for x in range(10):
    pameX = (x * 38) + 240
    pame_width = pame.get_width()
    pame_height = pame.get_height()
    pame_rect = Rect(pameX, pameY, pame_width, pame_height)
    pames.append(pame_rect)
agos = pygame.image.load('agos.png')
agoss = []
agosY = (orden[6]*45)+55
for x in range(10):
    agosX = (x * 38) + 240
    agos_width = agos.get_width()
    agos_height = agos.get_height()
    agos_rect = Rect(agosX, agosY, agos_width, agos_height)
    agoss.append(agos_rect)

while True:
    mainSurface.fill(black)
    #brick draw
    for b in paulas:
        mainSurface.blit(paula,b)
    for b in marias:
        mainSurface.blit(maria,b)
    for b in cars:
        mainSurface.blit(car,b)
    for b in agoss:
        mainSurface.blit(agos,b)
    for b in pames:
        mainSurface.blit(pame,b)
    for b in milis:
        mainSurface.blit(mili,b)
    for b in daniels:
        mainSurface.blit(daniel,b)
    #bat and ball draw
    mainSurface.blit(bat, batRect)
    mainSurface.blit(ball, ballRect)
    #events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
            if (mousex < 800 - 55):
                 batRect.topleft = (mousex, playerY)
            else:
                 batRect.topleft = (800 - 55, playerY)
        elif event.type == MOUSEBUTTONUP and not ballServed:
            ballServed = True
    #main game logic
    if ballServed:
        bx += sx
        by += sy
        ballRect.topleft = (bx, by)
    if (by <= 0):
        by = 0
        sy *= -1
    if (by >= 600 - 8):
        ballServed = False
        bx, by = (24, ballStartY)
        ballSpeed = 6
        sx, sy = (ballSpeed, ballSpeed)
        ballRect.topleft = (bx, by)
    if (bx <= 0):
        bx = 0
        sx *= -1
    if (bx >= 800 - 8):
        bx = 800 - 8
        sx *= -1
    if ballRect.colliderect(batRect):
        by = playerY - 8
        sy *= -1
    #collision detection
    paulaHitIndex = ballRect.collidelist(paulas)
    if paulaHitIndex >= 0:
        paulas_hb = paulas[paulaHitIndex]
        mx = bx + 4
        my = by + 4
        if mx > paulas_hb.x + paulas_hb.width or mx < paulas_hb.x:
            sx *= -1
        else:
            sy *= -1
        del (paulas[paulaHitIndex])
    mariaHitIndex = ballRect.collidelist(marias)
    if mariaHitIndex >= 0:
        marias_hb = marias[mariaHitIndex]
        mx = bx + 4
        my = by + 4
        if mx > marias_hb.x + marias_hb.width or mx < marias_hb.x:
            sx *= -1
        else:
            sy *= -1
        del (marias[mariaHitIndex])
    carHitIndex = ballRect.collidelist(cars)
    if carHitIndex >= 0:
        cars_hb = cars[carHitIndex]
        mx = bx + 4
        my = by + 4
        if mx > cars_hb.x + cars_hb.width or mx < cars_hb.x:
            sx *= -1
        else:
            sy *= -1
        del (cars[carHitIndex])
    pameHitIndex = ballRect.collidelist(pames)
    if pameHitIndex >= 0:
        pames_hb = pames[pameHitIndex]
        mx = bx + 4
        my = by + 4
        if mx > pames_hb.x + pames_hb.width or mx < pames_hb.x:
            sx *= -1
        else:
            sy *= -1
        del (pames[pameHitIndex])
    danielHitIndex = ballRect.collidelist(daniels)
    if danielHitIndex >= 0:
        daniels_hb = daniels[danielHitIndex]
        mx = bx + 4
        my = by + 4
        if mx > daniels_hb.x + daniels_hb.width or mx < daniels_hb.x:
            sx *= -1
        else:
            sy *= -1
        del (daniels[danielHitIndex])
    agosHitIndex = ballRect.collidelist(agoss)
    if agosHitIndex >= 0:
        agoss_hb = agoss[agosHitIndex]
        mx = bx + 4
        my = by + 4
        if mx > agoss_hb.x + agoss_hb.width or mx < agoss_hb.x:
            sx *= -1
        else:
            sy *= -1
        del (agoss[agosHitIndex])
    miliHitIndex = ballRect.collidelist(milis)
    if miliHitIndex >= 0:
        milis_hb = milis[miliHitIndex]
        mx = bx + 4
        my = by + 4
        if mx > milis_hb.x + milis_hb.width or mx < milis_hb.x:
            sx *= -1
        else:
            sy *= -1
        del (milis[miliHitIndex])
    pygame.display.update()
    fpsClock.tick(30)
