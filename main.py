import pygame
from P5game import *
pygame.display.set_caption("Game About Sentient Rocks!")
logicBtns={"and":BUTTON(0,300,50,30,(100,0,0),"AND",(0,0,0),textX=5,textY=5)}
running = True
while running:
    mouse.update()
    screen.fill((255, 255, 255))
    text(f"{mouse.leftPress} {mouse.rightPress} {mouse.leftClick} {mouse.rightClick} {mouse.leftWasPress} {mouse.rightWasPress}",0,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in logicBtns:
        logicBtns[i].disp()
        if logicBtns[i].activateLeft():print("ACTIVATED FOR",i)
    pygame.display.flip()

# Clean up
pygame.quit()