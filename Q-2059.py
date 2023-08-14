p, j1, j2, r, a = input().split()
p = int(p)
j1 = int(j1)
j2 = int(j2)
r = int(r)
a = int(a)
if p == 1: #par
    if (j1 + j2)%2 == 0:
        if r == a == 0:
            print("Jogador 1 ganha!")
        if r == 1 and a == 0:
            print("Jogador 1 ganha!")
        if r == 1 and a == 1:
            print("Jogador 2 ganha!")
        if r == 0 and a == 1:
            print("Jogador 1 ganha!")
    else:
        if r == a == 0:
            print("Jogador 2 ganha!")
        if r == 1 and a == 0:
            print("Jogador 1 ganha!")
        if r == 1 and a == 1:
            print("Jogador 2 ganha!")
        if r == 0 and a == 1:
            print("Jogador 1 ganha!")
else:
    if (j1 + j2)%2 == 0:
        if r == a == 0:
            print("Jogador 2 ganha!")
        if r == 1 and a == 0:
            print("Jogador 1 ganha!")
        if r == 1 and a == 1:
            print("Jogador 2 ganha!")
        if r == 0 and a == 1:
            print("Jogador 1 ganha!")
    else:
        if r == a == 0:
            print("Jogador 1 ganha!")
        if r == 1 and a == 0:
            print("Jogador 1 ganha!")
        if r == 1 and a == 1:
            print("Jogador 2 ganha!")
        if r == 0 and a == 1:
            print("Jogador 1 ganha!")    