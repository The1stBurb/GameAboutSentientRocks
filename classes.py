from P5game import *
from vars import *
class logicGateCondensed:
    def __init__(self,name,inputs,outputs,logic):
        self.name=name
        self.inps=inputs
        self.inpVal=[-1 for i in range(len(self.inps))]
        self.outs=outputs
        self.outVal=[-1 for i in range(len(self.inps))]
        self.logic=logic
    def render(self,x,y):
        ht=max(len(self.inps),len(self.outs))
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
    def update(self):
        pass
class Wire:
    def __init__(self,inputGateId,inputId,outputGateId,outputId):
        self.inpId=inputId
        self.inpGateId=inputGateId
        self.outId=outputId
        self.outGateId=outputGateId
        self.val=-1
    def update(self,gates,inps,outs):
        if self.inpGateId=="main":self.val=inps[self.inpId]
        else:self.val=gates[self.inpGateId].outs[self.inpId]
        if self.outGateId=="main":outs[self.outId]=self.val
        else:
            gates[self.outGateId].inps[self.outId]=self.val
            gates[self.outGateId].update(True)
    def render(self,gates,mainPos,inps,outs):
        if self.val==1:stroke(255,0,0)
        elif self.val==0:stroke(150,0,0)
        else:stroke(0)
        if self.inpGateId=="main":
            x1,y1=mainPos
            x1-=logicW
            y1+=list(inps).index(self.inpId)*logicIOsz
        else:
            x1,y1=gates[self.inpGateId].pos()
            y1+=(list(gates[self.inpGateId].outs).index(self.inpId)+0.5)*logicIOsz
        if self.outGateId=="main":
            x2,y2=mainPos
            x2+=logicW*logicW2
            y2+=list(outs).index(self.outId)*logicIOsz
        else:
            x2,y2=gates[self.outGateId].pos()
            y2+=(list(gates[self.outGateId].inps).index(self.outId)+0.5)*logicIOsz
        text(f"{x1+logicW} {y1} {x2} {y2}",0,200)
        line(x1+logicW,y1,x2,y2)

class LogicGate:
    def __init__(self,name,inputs={},outputs={},wires=[],gates={},logic="",x=0,y=0,inpos=[],outpos=[]):
        self.name=name
        self.inps=inputs
        self.inpos=inpos
        # self.inpVal=[-1 for i in range(len(self.inps))]
        self.outs=outputs
        self.outpos=outpos
        # self.outVal=[-1 for i in range(len(self.inps))]
        self.wires=wires
        self.gates=gates
        self.logic=logic
        self.x,self.y=x,y
    def renderAll(self):
        for i in self.wires:
            i.render(self.gates,(self.x,self.y),self.inps,self.outs)
        for i in self.gates:
            self.gates[i].renderSelf()
        for inp_y,i in enumerate(self.inps):
            if self.inps[i]==1:fill(255,0,0)
            elif self.inps[i]==0:fill(150,0,0)
            else:fill(0)
            ellipse(self.x,self.y+inp_y*logicIOsz,logicIOsz*0.7)
            text(self.inps[i],0,150+inp_y*20)
        for out_y,i in enumerate(self.outs):
            if self.outs[i]==1:fill(255,0,0)
            elif self.outs[i]==0:fill(150,0,0)
            else:fill(0)
            ellipse(self.x+logicW*logicW2,self.y+out_y*logicIOsz,logicIOsz*0.7)
    def renderSelf(self):
        ht=max(len(self.inps),len(self.outs))
        fill(200)
        rect(self.x,self.y,logicW,ht*logicIOsz)
        for inp_y,i in enumerate(self.inps):
            if self.inps[i]==1:fill(255,0,0)
            elif self.inps[i]==0:fill(150,0,0)
            else:fill(0)
            ellipse(self.x,self.y+(inp_y+0.5)*logicIOsz,logicIOsz*0.7)
        for out_y,i in enumerate(self.outs):
            if self.outs[i]==1:fill(255,0,0)
            elif self.outs[i]==0:fill(150,0,0)
            else:fill(0)
            ellipse(self.x+logicW,self.y+(out_y+0.5)*logicIOsz,logicIOsz*0.7)
        fill(0)
        text(self.name,self.x+10,self.y+10)
    def pos(self):
        return self.x,self.y
    def insertGate(self,gate,x,y):
        global logicGates,mouse
        gateID=getID()
        self.gates[gateID]=LogicGate(*logicGates[gate],x=x,y=y)
    def insertWire(self):
        pass
    def update(self,frmWire=False):
        global mouse
        # input(f"{self.name} , {self.wires} , {frmWire}")
        if mouse.leftClick:
            for inp_y,i in enumerate(self.inps):
                if dist(self.x,self.y+inp_y*logicIOsz,mouse.x,mouse.y)<logicIOsz*0.7:
                    # print("Yo it worked lol")
                    if self.inps[i]==0:self.inps[i]=1
                    else:self.inps[i]=0
                # ellipse(self.x,self.y+inp_y*logicIOsz,logicIOsz*0.7)
        # print(self.wires,"fish")
        for i in self.wires:
            # print(i)
            i.update(self.gates,self.inps,self.outs)
        if self.logic!="":
            logTmp=self.logic
            for i in self.inps:
                logTmp=logTmp.replace(i,str(self.inps[i]))
            # print(logTmp)
            logTmp=logTmp.replace("!","not").replace("&&","and").replace("||","or")
            self.outs["out"]=eval(logTmp)
        # for i in self.gates:
        #     self.gates[i].update()
def debug(*msg):
    print("BEBUG>> "," ".join([str(i) for i in msg]))