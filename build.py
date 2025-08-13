from classes import LogicGate,Wire,debug
from vars import logicGates
#"":{"inps":[":",":"],"outs":[":",":"],"truthTable":["00|","10|","01|","11|"],"info":"","notation":"&&"},
#logic is ifLogic[whatValueSHouldBe,whatValueToCheck] and if followed by a "." then that is IF ELSE, can be multi logics
gates={#"<math:not(a)|c>""<math:and(a,b)|c>""<math:not(and(a,b))|c>"["a,b,carryIn|c","000|00","100|10","010|10","110|01","001|10","011|01","101|01","111|11"]    
    "NOT":{"inps":["a:1"],"outs":["c:1"],"truthTable":["a|c","0|1","1|0"],"info":"The most basic Logic Gate, the NOT gate. It returns a 1 when a is 0, and a 0 when a is 1. Its notation is \"¬\" and the squigly thingy \"~\" (why does this exsist)."},#,"notation":"!"
    "AND":{"inps":["a:1","b:1"],"outs":["c:1",],"truthTable":["a,b|c","00|0","10|0","01|0","11|1"],"info":"This is an AND gate. It gives a 1 when a AND b are 1. The notation used is \"^\" or a \"*\" (which I like more), the multiplication symbol, because 0*0, 0*1, and 1*0=0, but 1*1=1."},
    "NAND":{"inps":["a:1","b:1"],"outs":["c:1",],"truthTable":["a,b|c","00|1","10|1","01|1","11|0"],"info":"This one you have. It is an AND gate with a NOT tacked on to the output, and so giving a 1 unless a AND b are 1. This is it's notationm, \"↓\", which I don't understand."},
    "OR":{"inps":["a:1","b:1"],"outs":["c:1",],"truthTable":["a,b|c","00|0","10|1","01|1","11|1"],"info":"This is an OR gate. It gives a 1 when a OR b is 1. The notation used is \"v\" or \"+\" (which i like better), because 0+0=0, but 1+0, 0+1, and (aparently) 1+1=1."},
    "NOR":{"inps":["a:1","b:1"],"outs":["c:1",],"truthTable":["a,b|c","00|1","10|0","01|0","11|0"],"info":"This is a NOR gate. Its like the NAND gate, but has an OR with a NOT-ed output. It gives an 1 when a AND b are 0. The notation used is wacky like NAND's, being \"↑\"."},
    "XOR":{"inps":["a:1","b:1"],"outs":["c:1",],"truthTable":["a,b|c","00|0","10|1","01|1","11|0"],"info":"This is an XOR gate, or Exclusive OR. It returns a 1 when a OR b is 1 AND a≠b (not equal). It has a slightly sense making symbol, \"⊕\"."},
    "XNOR":{"inps":["a:1","b:1"],"outs":["c:1",],"truthTable":["a,b|c","00|1","10|0","01|0","11|1"],"info":"Then, last of the basic Logic Gates, the XNOR. If you couldn't guess, a XOR with a NOT-ed output. It returns a 1 when a=b. It's notation is \"↔\"."},
    "1BitAdder":{"inps":["a:1","b:1","carryIn:1"],"outs":["sum:1","carryOut:1"],"truthTable":"math:a+b|sum;max:1|carryOut","info":"This is used to add single bit numbers together (1 or 0). Its not very useful, but when you have 8 or 16 or 32, now you can add numbers as bIg as 256 or 65,536 or 4,294,967,296. yay. It has 2 inputs and a carryIn/Out. The carry is used the same way it is in decimal arithmetic: if you have 2 numbers (lets say 14 and 8), well those make 22, which is bigger than 9. If there is no carry, 14+8=2 which is not right. The carry would tell us \"HEY you made a BIG number so add a 1 to the next columns calculations!\". Here, the hooman would add 4+8=2, carry 1. we carry the one and get 1 (that was carried) +1+0=2. now we then get 22 yay all is not lost"},
    "8BitAdder":{"inps":["a:8:","b:8","carryIn:1"],"outs":["sum:8","carryOut:1"],"truthTable":"math:a+b|sum;max:2^8|carryOut","info":"Yea, i seriously hope this isn't too hard... (dont worry if you mess up the carrys lol i do)","notation":"&&"},
    "ALU-V1":{"inps":["a:8","b:8","op:1"],"outs":["c8","carry:1","zero:1"],"truthTable":"math:op=0?a+b:a-b|sum;max:2^8|carry<min:0|zero","info":"This is a Arithmetic Logic Unit, but slightly boring. We'll make better versions later! All this does is Addition if op is 0, Subtraction if op is 1. The Carry flag activates if it the adder overflows (aka making a number above 255 aka the carry out on the MSB is 1). The Zero flag activates if the sum is 0 (wow crazy)"},
    "1BitSet":{"inps":["data:1","set:1"],"outs":["dataOut:1",],"truthTable":["data,set,dataOut|dataOut","000|0","100|0","i11x|x","001|1","101|1","01x|0","11x|1"],"info":"This is the simplest for of memory. When set is 0, it does not matter what data is, dataOut will stay the same. But, when set is 1, dataOut will change to be whatever data is!","notation":"&&"},
    "1BitEnable":{"inps":["data:1","enable:1"],"outs":["dataOut:1",],"truthTable":["data,enable|dataOut","00|0","10|0","01|0","11|1"],"info":"This only lets data \"out\" when enable is 1. You might want to take a look at the other Truth Tables...","notation":"&&"},
    "1BitMemory":{"inps":["data:1","set:1","enable:1"],"outs":["enableBypass:1","dataOut:1",],"truthTable":"<logic:set=1 and enable=1[data|dataOut].enable=1[enableBypass|dataOut].set=1[data|enableBypass]]>","info":"Just put a 1BitSet and 1BitEnable together!","notation":"&&"},
    "Stepper5":{"inps":["clock:1","reset:1"],"outs":["step1:1","step2:1","step3:1","step4:1","step5:1"],"truthTable":["clock,reset,step1,step2,step3,step4,step5|step1,step2,step3,step4,step5","1010000|01000","1001000|00100","1000100|00010","1000010|0001","1000001|10000","X1XXXXX|10000",],"info":"","notation":"&&"},
    # "clock":{"inps":["",""],"outs":["",""],"truthTable":["|","|"]},
}

class Gates:
    def __init__(self,inps,outs,truthTable,info):
        self.inps,self.outs,self.truth,self.info=inps,outs,truthTable,info
    def checks(self,gate):
        log=[]
        ttMap=self.truth[0].split("|")
        ttMap=[ttMap[0].split(","),ttMap[1].split(",")]
        # ttMapIn,ttMapOut=ttMapIn.split(","),ttMapOut.split(",")
        checkRet=self.checkBase(gate,self.truth[1],ttMap)
        log.append(checkRet)
        debug(ttMap)
        debug("checks LOG",log)
        pass
    def checkBase(self,gate,tt,ttMap):
        log=[]
        inp,out=tt.split("|")
        for i in range(len(inp)):
            if ttMap[0][i]in gate.inps:
                gate.inps[ttMap[0][i]]=int(inp[i])
                log.append(f"Input gate \"{ttMap[0][i]}\" is now a <{inp[i]}>")
            elif ttMap[0][i]in gate.outs:
                if gate.outs[ttMap[0][i]]==int(inp[i]):
                    log.append(f"Out gate \"{ttMap[0][i]}\" matches! Read a <{inp[i]}>")
                else:
                    log.append(f"Out gate \"{ttMap[0][i]}\" incorrect! Read a <{gate.inps[ttMap[0][i]]}>, needed a <{inp[i]}>.")
                    return "badMatchOutput",log
        gate.update()
        for i in range(len(out)):
            if ttMap[1][i]in gate.inps:
                pass
            elif ttMap[1][i]in gate.outs:
                if gate.outs[ttMap[1][i]]==int(out[i]):
                    log.append(f"Output \"{ttMap[1][i]}\" was succesful! Read a <{out[i]}>")
                else:
                    log.append(f"Output \"{ttMap[1][i]}\" was unsuccesful. Read a <{gate.outs[ttMap[1][i]]}>, needed a <{out[i]}>.")
                    return "badOutput",log
        debug("checkBase LOG",log)
# print(**gates["NOT"])
nt=LogicGate("not",{"a":0},{"c":0},[],{},"",0,0)
nt.insertGate("nand",30,10)
nm=list(nt.gates)[0]
# baseGate.gates[getID()]=LogicGate(*logicGates["nand"],x=30,y=10)
# print(baseGate.gates[nm].wires)
nt.wires.append(Wire("main","a",nm,"b"))
nt.wires.append(Wire("main","a",nm,"a"))
nt.wires.append(Wire(nm,"out","main","c"))
g=Gates(**gates["NOT"])
g.checks(nt)
#"":{"descrip":"","level":""},
automation={
    "buyer1":{"descrip":"Buys things automatically, but not very reliable cause your not paying them and they don't know what their doing.","level":"Unpaid Intern"},
    "buyer2":{"descrip":"Buys things automatically, but you have to pay them at least the minumum wage. They also actually know what their doing (mostly).","level":"Intern"},
    "buyer3":{"descrip":"Buys things automatically, but you pay them more and they do good.","level":"Job"},
    "buyer4":{"descrip":"They make sure the people buying things automatically are actually buying things automatically.","level":"Manager"},
    "buyer5":{"descrip":"They make sure the people making sure the people buying things automatically are making sure the people are buying things automatically.","level":"Head Manager"},
    "buyer6":{"descrip":"They make sure the last one does what they need to do.","level":"CEO"},
    "maker1":{"descrip":"Makes chips based on fabrication requirements.","level":"Job"},
    "maker2":{"descrip":"Makes sure the people making chips make the chips.","level":"Manager"},
    "maker3":{"descrip":"Makes sure the people making sure the people making the chips make sure the people making the chips make the chips.","level":"Head Manager"},
    "maker4":{"descrip":"Makes everyone make chips!","level":"CEO"},
    "greg":{"descrip":"He is Greg...","level":"skorpl "},
    "ship1":{"descrip":"Loads and sends the finished products off to the selling place.","level":"Job"},
    "ship2":{"descrip":"Loads and sends the people who should be loading and sending the products but aren't to the selling place.","level":"Manager"},
    "ship3":{"descrip":"Makes sure we're not losing people to the selling place...","level":"CEO"},

    "buyerBot1":{"descrip":"Buys things automatically, but you have to don't have to pay them anything. They aren't very good tho.","level":"Intern"},
    "buyerBot2":{"descrip":"Buys things automatically, but you pay them none and they do good.","level":"Job"},
    "buyerBot3":{"descrip":"Buys things better automatically.","level":"Manager"},
    "buyerBot4":{"descrip":"Buys things best automatically.","level":"Head Manager"},
    "buyerBot5":{"descrip":"Buys things bester automatically.","level":"CEO"},
    "makerBot1":{"descrip":"Makes chips based on your orders.","level":"Job"},
    "makerBot2":{"descrip":"Makes chips but better.","level":"Manager"},
    "makerBot3":{"descrip":"Makes chips buts best.","level":"Head Manager"},
    "makerBot4":{"descrip":"Makes chips but bester.","level":"CEO"},
    "gregBot":{"descrip":"He is Greg... But a bot...","level":"skorpl "},
    "shipBot1":{"descrip":"Loads and sends the finished products off to the selling place.","level":"Job"},
    "shipBot2":{"descrip":"Loads and sends but better.","level":"Manager"},
    "shipBot3":{"descrip":"Loads and sends but best.","level":"CEO"},
}