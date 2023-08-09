
def primo(val):
    if val <= 1:
        return False
    if val <= 3:
        return True
    if val % 2 == 0 or val % 3 == 0:
        return False
    
    i = 5
    while i * i <= val:
        if val % i == 0 or val % (i + 2) == 0:
            return False
        i += 6
    
    return True

def gemeo(vetor,cont):
    gem = []
    A = 0
    for i in range (cont):
        if i == (cont-1):
            if abs(vetor[i]-vetor[i-1]) == 2:
                if vetor[i] not in gem:
                    gem.append(vetor[i])
                    A+=1
            if abs(vetor[i] - proximoprim(vetor[i])) == 2:
                if vetor[i] not in gem:
                    gem.append(vetor[i])
                    A+=1
        else:
            if abs(vetor[i]-vetor[i+1]) == 2:
                if vetor[i] not in gem:
                    gem.append(vetor[i])
                    A+=1
                if vetor[i+1] not in gem:
                    gem.append(vetor[i+1])
                    A+=1
            elif abs(vetor[i]-proximoprimm(vetor[i])) == 2:
                if vetor[i] not in gem:
                    gem.append(vetor[i])
                    A+=1                
            
    return A


def proximoprim(A):
    prox = A + 1
    while True:
        if primo(prox):
            return prox
        prox += 1

def proximoprimm(A):
    prox = A - 1
    while True:
        if primo(prox):
            return prox
        prox -= 1
        if prox <= 0:
            break
    return A

for i in range (0,int(input())):
    gemeos = 0
    primos = []
    cont = 0
    X, Y = map(int,input().split())
    for i in range (X, Y+1):
        if primo(i):
            primos.append(i)
            cont+=1
    gemeos = gemeo(primos, cont)
    print(gemeos)

