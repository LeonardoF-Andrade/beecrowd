import sys

def primo(val, p):
    print(n)
    if val in p:
        return True
    if val in n:
        return False
    if val <= 1:
        n.append(val)
        return False
    if val <= 3:
        p.append(val)
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
    
    p.append(val)
    return True

def gemeo(vetor,cont, gem):
    A = 0
    cont2 = 0
    for i in range (cont):
        if vetor[i] in gem and cont2 == 0:
            A +=1
        elif i == (cont-1):
            if abs(vetor[i]-vetor[i-1]) == 2:
                if vetor[i] not in gem:
                    gem.append(vetor[i])
                    A+=1
            if abs(vetor[i] - proximoprim(vetor[i])) == 2:
                if vetor[i] not in gem:
                    gem.append(vetor[i])
                    A+=1
        else:
            cont2 = 0
            if abs(vetor[i]-vetor[i+1]) == 2:
                if vetor[i] not in gem:
                    gem.append(vetor[i])
                    A+=1
                if vetor[i+1] not in gem:
                    gem.append(vetor[i+1])
                    cont2 +=1
                    A+=1
            elif abs(vetor[i]-proximoprimm(vetor[i])) == 2:
                if vetor[i] not in gem:
                    gem.append(vetor[i])
                    A+=1                
            
    return A, gem


def proximoprim(A):
    prox = A + 1
    while True:
        if prox > A+2:
            return A
        if primo(prox,pr):
            return prox
        prox += 1

def proximoprimm(A):
    prox = A - 1
    while True:
        if prox < A-2:
            return A
        if primo(prox,pr):
            return prox
        prox -= 1
        if prox <= 0:
            break
    return A

gemeos = []
pr = []
n = []

for i in range (0,int(input())):
    primos = []
    cont = 0
    X, Y = map(int, sys.stdin.readline().strip().split())
    for i in range (X, Y+1):
        if primo(i,pr):
            primos.append(i)
            cont+=1
    j , gemeos = gemeo(primos, cont, gemeos)
    print(j)

