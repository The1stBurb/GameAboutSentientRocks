import pygame
from P5game import *
from random import choice
from classes import *
from vars import *
pygame.display.set_caption("Game About Sentient Rocks!")
logicBtns={"nand":BUTTON(0,300,50,30,(100,0,0),"NAND",(0,0,0),textX=5,textY=5)}
strokeWeight(5)

baseGate=LogicGate("Main",{"a":0,"b":0},{"c":0},x=0,y=10)
baseGate.insertGate("nand",30,10)
nm=list(baseGate.gates)[0]
# baseGate.gates[getID()]=LogicGate(*logicGates["nand"],x=30,y=10)
# print(baseGate.gates[nm].wires)
baseGate.wires.append(Wire("main","a",nm,"b"))
baseGate.wires.append(Wire("main","b",nm,"a"))
baseGate.wires.append(Wire(nm,"out","main","c"))
running = True
kbrd=[""]
while running:
    mouse.update()
    screen.fill((255, 255, 255))
    text(f"{mouse.leftPress} {mouse.rightPress} {mouse.leftClick} {mouse.rightClick} {mouse.leftWasPress} {mouse.rightWasPress}",0,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type==pygame.KEYDOWN and kbrd[-1]!=pygame.key.name(event.key):
            kbrd.append(pygame.key.name(event.key))
    baseGate.renderAll()
    pygame.display.flip()
    baseGate.update()
    for i in logicBtns:
        logicBtns[i].disp()
        if logicBtns[i].activateLeft():print("ACTIVATED FOR",i)
    pygame.display.flip()
    if len(kbrd)>2:
        if kbrd[-1]=="s" and kbrd[-2]=="ctrl":
            logicGates[baseGate.name]=(baseGate.name,baseGate.inps,baseGate.outs,baseGate.wires,baseGate.gates,baseGate.logic)
            baseGate=LogicGate("Unamed",x=0,y=10)
# Clean up
pygame.quit()