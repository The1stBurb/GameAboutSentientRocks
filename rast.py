from math import cos,sin
from P5game import *
from random import randint
class camera:
    def __init__(self,x,y,z,xa,ya,za):
        self.x,self.y,self.z=x,y,z
        self.xa,self.ya,self.za=xa,ya,za
    def step(self):
        pass
        # self.x+=sin(self.xa)*10
        # self.y+=sin(self.ya)
        # if self.xa==0:self.xa=0.0001
        # if self.ya==0:self.ya=0.0001
        # if self.za==0:self.za=0.0001
cm=camera(100,100,0,0,0,0)
# import math

def rotate_xyz(v, phi, theta, psi):
    x, y, z = v
    s1, c1 = sin(phi),   cos(phi)    # φ = roll (X)
    s2, c2 = sin(theta), cos(theta)  # θ = pitch (Y)
    s3, c3 = sin(psi),   cos(psi)    # ψ = yaw (Z)

    # combined rotation matrix entries:
    r11 =  c3*c2
    r12 =  c3*s2*s1 - s3*c1
    r13 =  c3*s2*c1 + s3*s1

    r21 =  s3*c2
    r22 =  s3*s2*s1 + c3*c1
    r23 =  s3*s2*c1 - c3*s1

    r31 = -s2
    r32 =  c2*s1
    r33 =  c2*c1

    x_p = r11*x + r12*y + r13*z
    y_p = r21*x + r22*y + r23*z
    z_p = r31*x + r32*y + r33*z

    return (x_p, y_p, z_p)

class obj:
    def __init__(self,x,y,z,vrtx):
        self.x,self.y,self.z,self.vrtx=x,y,z,vrtx
    def disp(self,cam):
        vrtxs=self.project(cam)
        # line(20,20,vrtxs[0][0],vrtxs[0][1])
        # for x,i in enumerate(vrtxs):
        #     line(20+x*10,20,i[0],i[1])
        #     ellipse(i[0],i[1],5,5)
        for i in range(len(vrtxs)-1):
            if vrtxs[i][2]<cam.z*sin(cam.za) or vrtxs[i+1][2]<cam.z*sin(cam.za):continue
            line(vrtxs[i][0],vrtxs[i][1],vrtxs[i+1][0],vrtxs[i+1][1])
        line(vrtxs[-1][0],vrtxs[-1][1],vrtxs[0][0],vrtxs[0][1])
    def project(self,cam):
        vrtx=[]
        sz=20
        scl=100
        for v in self.vrtx:
            vx,vy,vz=v
            nx,ny,nz=rotate_xyz(((vx*sz)+self.x-cam.x,(vy*sz)+self.y-cam.y,(vz*sz)+self.z-cam.z),cam.xa/scl,cam.ya/scl,cam.za/scl)
            vrtx.append((nx+cam.x,ny+cam.y,nz+cam.z))
            # sx,cx,sy,cy,sz,cz=sin(cam.xa/scl),cos(cam.xa/scl),sin(cam.ya/scl),cos(cam.ya/scl),sin(cam.za/scl),cos(cam.za/scl)
            # vrtx.append(((cz*cy*nx+(cz*sy*sx - sz*cx)*ny+(cz*sy*cx + sz*sx)*nz+cam.x),(sz*cy*nx+(sz*sy*sx + cz*cx)*ny+(sz*sy*cx - cz*sx)*nz+cam.y),(-sy*nx+(cy*sx)*ny+(cy*cx)*nz+cam.z)))
        return vrtx
o=obj(100,100,-20,[(-1,-1,-1),(1,-1,-1),(-1,1,-1),(1,1,-1),(-1,-1,1),(1,-1,1),(-1,1,1),(1,1,1)])
while True:
    mouse.update()
    cm.step()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    fill(randint(0,255))
    o.disp(cm)
    ellipse(width/2,height/2,5,5)
    pygame.display.flip()
    cm.ya=mouse.x+width/2
    cm.za=mouse.y+height/2
    
