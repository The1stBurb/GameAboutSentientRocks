import pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

pygame.font.init()
FONT_SIZE=20
font = pygame.font.SysFont(None, FONT_SIZE)


COLOUR=(0,0,0)
STROKE=(0,0,0)
STROKE_WEIGHT=1
def fill(r,g=False,b=False):
    global COLOUR
    if isinstance(r,tuple):r,g,b=r
    if g==False and b==False:g=b=r
    COLOUR=(r,g,b)
def stroke(r,g=False,b=False):
    global STROKE
    if g==False and b==False:g=b=r
    STROKE=(r,g,b)
def strokeWeight(val):
    global STROKE_WEIGHT
    STROKE_WEIGHT=val
def rect(x,y,w,h):
    pygame.draw.rect(screen, COLOUR, (x, y, w, h))
def ellipse(x,y,w,h=False):
    if h==False:h=w
    pygame.draw.ellipse(screen, COLOUR, (x-w/2, y-h/2, w, h))
# def tri(x1,y1,x2,y2,x3,y3):

def line(x1,y1,x2,y2):
    pygame.draw.line(screen, STROKE, (x1, y1), (x2, y2), STROKE_WEIGHT)
def text(txt,x,y,centerX=False,centerY=False,shadow=False,rightAlign=False,bottomAlign=False):
    if shadow:shdwTxt=font.render(txt,True,(0,0,0))
    txt=font.render(txt,True,COLOUR)
    pos=txt.get_rect()
    if centerX:pos.centerx=x
    elif rightAlign:pos.right=x
    else:pos.x=x
    if centerY:pos.centery=y
    elif bottomAlign:pos.bottom=y
    else:pos.y=y
    if shadow:
        shdwPos=pos.copy()
        shdwPos.y+=1
        shdwPos.x+=1
        screen.blit(shdwTxt,shdwPos)
    screen.blit(txt,pos)
def textSize(val):
    global font,FONT_SIZE
    FONT_SIZE=val
    font=pygame.font.SysFont(None,val)
class BUTTON:
    def __init__(self,x,y,w,h,col,txt,textCol,textX=False,textY=False,adaptive=False):
        self.x,self.y,self.w,self.h,self.col=x,y,w,h,col
        self.txt,self.txtcol=txt,textCol
        self.txtx=0 or textX
        self.txty=0 or textY
        self.adapt=adaptive
        # self.h=len(self.txt*FONT_SIZE)
    def disp(self):
        fill(self.col)
        if self.hover() and self.adapt:rect(self.x-2,self.y-2,self.w+4,self.h+4)
        else:rect(self.x,self.y,self.w,self.h)
        fill(self.txtcol)
        text(self.txt,self.x+self.txtx,self.y+self.txty)
    def activateRight(self):
        global mouse
        if self.hover() and mouse.rightClick:return True
        return False
    def activateLeft(self):
        global mouse
        if self.hover() and mouse.leftClick:return True
        return False
    def hover(self):
        global mouse
        if mouse.x>=self.x and mouse.y>=self.y and mouse.x<=self.x+self.w and mouse.y<=self.y+self.h:return True
        return False

class MOUSE:
    def __init__(self):
        self.x,self.y=0,0
        self.rightPress=False
        self.leftPress=False
        self.rightClick=False
        self.leftClick=False
        self.rightWasPress=False
        self.leftWasPress=False
    def update(self):
        self.x,self.y=pygame.mouse.get_pos()
        mse_btns=pygame.mouse.get_pressed()
        self.leftPress=mse_btns[0]
        self.rightPress=mse_btns[2]
        if self.leftPress:
            if not self.leftWasPress:self.leftClick=self.leftWasPress=True
            else:self.leftClick=False
        else:self.leftWasPress=False
        if self.rightPress:
            if not self.rightWasPress:self.rightClick=self.rightWasPress=True
            else:self.rightClick=False
        else:self.rightWasPress=False
mouse=MOUSE()