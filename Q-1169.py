i = int(input())

for j in range (i):
    aux = 1
    p = int(input())
    for x in range (p):
        aux = aux*2
    aux = aux//12
    aux = aux//1000
    print(aux,"kg")