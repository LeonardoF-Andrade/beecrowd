import sys
import random

def primo(val, z, w, flag = True, k = 5):
    global Aux, cont, primos
    if val in gemeos and val not in primos:
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
       gemeos.append(val)
       return True
    if val <= 3 and flag:
        if val == z:
            if cont == 0:
               if val <= z or val >= w:
                Aux += 1
               pr.append(val)
               return True
            if abs(val - proximoprimm(val)) == 2 :
                if val not in gemeos:
                 gemeos.append(val)
                 if val <= z or val >= w:
                  Aux += 1
            elif abs(val - proximoprim(val)) == 2:
                if val not in gemeos:
                  gemeos.append(val)
                  if val <= z or val >= w:
                     Aux += 1
            pr.append(val)
            return True
        elif cont == 0:
         if abs(val - proximoprim(val)) == 2:
            if val not in gemeos:
                gemeos.append(val)
                if val <= z or val >= w:
                    Aux += 1
        elif val < z:
            if abs(val - proximoprim(val)) == 2:
                 if val not in gemeos:
                    gemeos.append(val)
                    if val <= z or val >= w:
                     Aux += 1
        pr.append(val)
        return True
    if val % 2 == 0 or val % 3 == 0 :
     n.append(val)
     return False
    
    for i in range(3, cont):
       if val != primos[i] and val % primos[i] == 0:
          n.append(val)
          return False

    if flag == False:
       gemeos.append(val)
       return True

    if val == z:
        if cont == 0:
            if val <= z or val >= w:
             Aux += 1
            pr.append(val)
            return True
        if abs(val - proximoprimm(val)) == 2:
            if val not in gemeos:
                gemeos.append(val)
                if val <= z or val >= w:
                 Aux += 1
        elif abs(val - proximoprim(val)) == 2:
         if val not in gemeos:
            gemeos.append(val)
            if val <= z or val >= w:
                Aux += 1
        pr.append(val)
        return True
    elif cont == 0:
        if abs(val - proximoprim(val)) == 2:
         if val not in gemeos:
            gemeos.append(val)
            if val <= z or val >= w:
                Aux += 1
    elif val < z:
        if abs(val - proximoprim(val)) == 2:
                if val not in gemeos:
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


for _ in range (0,int(input())):
    primos = []
    Aux = 0
    cont = 0
    X, Y = map(int, sys.stdin.readline().strip().split())
    for i in range (X, Y+1):
         if primo(i, max(Y,X), min(X, Y)):
            primos.append(i)
            cont +=1       
    print(Aux)

