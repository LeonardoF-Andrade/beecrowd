ho =0
hu = 0
el = 0
an = 0
ma = 0

i=int(input())

for j in range (0,i):
    N, C = input().split()
    if C == "X":
        ho+=1
    elif C == "M":
        ma+=1
    elif C == "H":
        hu+=1
    elif C == "E":
        el+=1
    elif C == "A":
        an +=1

print(f"{ho} Hobbit(s)\n{hu} Humano(s)\n{el} Elfo(s)\n{an} Anao(oes)\n{ma} Mago(s)")