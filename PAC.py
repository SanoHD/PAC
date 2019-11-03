import os, sys, shlex
from random import *

var = {}
commentsymbol = ";"
filename = "code.txt"
errors = ["Damn! I can´t ","I can´t ","Seems like i can´t ","eehhh we´ve got a problem. I can´t "]
goto = {}

def error(txt="do this."):
    global LN
    print("\n[PAC-ERROR] Line("+str(LN)+")",choice(errors)+txt)
    sys.exit()

def i(t):
    if gline[:len(t)] == t:
        return True
    else:
        return False

def getgoto():
    ingoto = False
    file = open(filename)
    LN = 0
    for line in file:
        LN += 1
        line = line.strip()
        if line == "" or line[0] == ";":
            continue
        if line[0] == "*":
            goto[line[1:]] = LN
    file.close()

getgoto()

def parser(line):
    global gline, loop
    gline = line
    sline = line.split()
    ssline = shlex.split(line)

    line = line.replace("\\n","\n")

    if i("OPEN "):
        var[sline[1]] = 0

    elif i("USE ") and sline[2] == "WITH":
        num = int(sline[1])
        vn = sline[3]
        if vn in var:
            var[vn] = num
        else:
            error("use an undefined variable.")

    elif i("TALK "):
        if line[5] == "\"" and line[-1] == "\"":
            print(line[6:-1],end="")
        else:
            vn = sline[1]
            if vn[0] == "#":
                if vn[1:] in var:
                    print(var[vn[1:]],end="")
                else:
                    error("output an undefined variable.")
            else:
                if vn in var:
                    print(chr(var[vn]),end="")
                else:
                    error("output an undefined variable.")


    elif i("PUSH "):
        vn = sline[1]
        if vn in var:
            var[vn] = var[vn] + 1
        else:
            error("push an undefined variable.")

    elif i("PULL "):
        vn = sline[1]
        if vn in var:
            var[vn] = var[vn] - 1
        else:
            error("pull an undefined variable.")

    elif i("GIVE "):
        vn = sline[1]
        if vn in var:
            try:
                var[vn] = int(input())
            except:
                error("input a string/float.")
        else:
            error("input to an undefined variable.")

    elif i("WALK TO "):
        to = line[8:]
        if to in goto:
            tLN = goto[to]
            loop = True
            while loop:
                try:
                    parser(fr[tLN-1])
                    tLN += 1
                except RecursionError:
                    error("walk to the same point every time.")
        else:
            error("goto an undefined location.")

    elif i("TURN OFF "):
        a = sline[2] # if a > b
        b = sline[3]
        if a in var and b in var:
            if int(var[a]) == int(var[b]):
                loop = False
        else:
            error("check undefined variables.")
    

LN = 0
file = open(filename)
fr = file.read().split("\n")
file = open(filename)
for L in file:
    LN += 1
    L = L.strip()
    if L != "" and L[:len(commentsymbol)] != commentsymbol:
        parser(L)
    else:
        continue

"""
PICKUP / WALK TO -> FUNCTIONS



"""
