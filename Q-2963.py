from sys import stdin

candidatos = int(stdin.readline())
numvotes = 0
maiorvoto = 0
carlos = 0
votos = 0
for i in range(candidatos):
    if i == 0:
        carlos = int(stdin.readline())
    else:
        votos = int(stdin.readline())
        if votos>maiorvoto:
            maiorvoto=votos
        if maiorvoto>carlos:
            break

        numvotes+=votos
    if numvotes>100000:
        break
    if carlos>=50000:
        break
if carlos>=maiorvoto:
    print('S')
else:
    print("N")