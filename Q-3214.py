
E, F, C = list(map(int, input().split()))

E = E + F
cont = 0
while E != 0:
    aux = E//C
    cont = cont + aux
    E = E%C
    if aux+E >= C:
        E = E + aux
    else: 
        break

print(cont)