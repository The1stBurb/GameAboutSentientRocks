import pygame
from P5game import *
from random import choice
pygame.display.set_caption("Game About Sentient Rocks!")
allIDs=[]
charID="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
def getID(chars=5):
    newID=""
    for i in chars:
        newID+=choice(charID)
    if newID in allIDs:
        return getID(chars)
    return newID
logicBtns={"nand":BUTTON(0,300,50,30,(100,0,0),"NAND",(0,0,0),textX=5,textY=5)}
logicIOsz=20
class logicGateCondensed:
    def __init__(self,name,inputs,outputs,logic):
        self.name=name
        self.inps=inputs
        self.inpVal=[-1 for i in range(len(self.inps))]
        self.outs=outputs
        self.outVal=[-1 for i in range(len(self.inps))]
        self.logic=logic
    def render(self,x,y):
        ht=max(len(self.inps,self.outs))
        fill(200)
        rect(x,y,100,ht*logicIOsz)
        for inp_y,i in enumerate(self.inpVal):
            if i==1:fill(255,0,0)
            elif i==0:fill(150,0,0)
            else:fill(0)
            ellipse(x,y+inp_y*logicIOsz,logicIOsz*1.5)
        for out_y,i in enumerate(self.outVal):
            if i==1:fill(255,0,0)
            elif i==0:fill(150,0,0)
            else:fill(0)
            ellipse(x+100,y+out_y*logicIOsz,logicIOsz*1.5)
class Wire:
    def __init__(self,inputId,outputId):

class LogicGate:
    def __init__(self,name,inputs,outputs,wires,gates):
        self.name=name
        self.inps=inputs
        self.inpVal=[-1 for i in range(len(self.inps))]
        self.outs=outputs
        self.outVal=[-1 for i in range(len(self.inps))]
        self.wires=wires
        self.gates=gates
logicGates={"nand":logicGateCondensed("NAND",["a","b"],["out"],"not(a and b)")}
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