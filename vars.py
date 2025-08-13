from random import choice
allIDs=[]
charID="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
def getID(chars=5):
    newID=""
    for i in charID:
        newID+=choice(charID)
    if newID in allIDs:
        return getID(chars)
    return newID

logicIOsz=20
logicW=70
logicW2=10

logicGates={"nand":("NAND",{"a":0,"b":0,},{"out":0},[],{},"!(a && b)")}#,"not(a and b)")}