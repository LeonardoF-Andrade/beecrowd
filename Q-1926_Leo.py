import sys

def primo(val, z, w, flag = True):
    global Aux, cont
    print("FFFFFF")
    print(val, gemeos, primos, Aux)
    if val in gemeos:
        Aux += 1
        return True
    if val in pr:
        return True
    if val in n:
        return False
    if val <= 1:
        n.append(val)
        return False
    if val <= 3 and flag == False:
       return True
    if val <= 3 and flag:
        if val == z:
            if cont == 0:
               print("AA")
               if val <= z or val >= w:
                Aux += 1
               pr.append(val)
               return True
            if abs(val - proximoprimm(val)) == 2 :
                if val not in gemeos:
                 print("BB")
                 gemeos.append(val)
                 if val <= z or val >= w:
                  Aux += 1
            pr.append(val)
            return True
        elif cont == 0:
         if abs(val - proximoprim(val)) == 2:
            if val not in gemeos:
                print("CC")
                gemeos.append(val)
                if val <= z or val >= w:
                    Aux += 1
        elif val < z:
            if abs(val - proximoprim(val)) == 2:
                 if val not in gemeos:
                    print("DD")
                    gemeos.append(val)
                    if val <= z or val >= w:
                     Aux += 1
        pr.append(val)
        return True
    if val % 2 == 0 or val % 3 == 0:
     n.append(val)
     return False
    
    i = 5
    while i * i <= val:
        if val % i == 0 or val % (i + 2) == 0:
            n.append(val)
            return False
        i += 6  

    if val == z:
        if cont == 0:
            if val <= z or val >= w:
             Aux += 1
             print("EE")
            pr.append(val)
            return True
        if abs(val - proximoprimm(val)) == 2 :
            if val not in gemeos:
                print("FF")
                gemeos.append(val)
                if val <= z or val >= w:
                 Aux += 1
        pr.append(val)
        return True
    elif cont == 0:
        if abs(val - proximoprim(val)) == 2:
         if val not in gemeos:
            print("GG")
            gemeos.append(val)
            if val <= z or val >= w:
                Aux += 1
    elif val < z:
        if abs(val - proximoprim(val)) == 2:
                if val not in gemeos:
                 print("HH")
                 gemeos.append(val)
                if val <= z or val >= w:
                    Aux += 1
    pr.append(val)
    return True


def proximoprim(A):
    global X, Y 
    prox = A + 1
    while True:
        if prox > (A+2):
            return A
        if primo(prox,Y,X,False):
            return prox
        prox += 1

def proximoprimm(A):
    global X, Y
    prox = A - 1
    while True:
        if prox < (A-2):
            return A
        if primo(prox,Y,X,False):
            return prox
        prox -= 1
        if prox <= 1:
            break
    return A

gemeos = []
pr = []
n = []


for i in range (0,int(input())):
    primos = []
    Aux = 0
    cont = 0
    X, Y = map(int, sys.stdin.readline().strip().split())
    for i in range (X, Y+1):
        if primo(i, Y, X):
            primos.append(i)
            cont +=1
    print(Aux)

