a = int(input())

Ra = "rajesh"
Sh = "sheldon"

for i in range(0,a):
    R, S = input().split()
    if R == "tesoura":
        R = 1
    elif R == "pedra":
        R = 2
    elif R == "papel":
        R = 3
    elif R == "lagarto":
        R = 4
    elif R == "spock":
        R = 5
    if S == "tesoura":
        S = 1
    elif S == "pedra":
        S = 2
    elif S == "papel":
        S = 3
    elif S == "lagarto":
        S = 4
    elif S == "spock":
        S = 5
    if S == R:
        print("empate")
    else:
        if R == 1 and (S == 3 or S == 4):
            print(Ra)
        if R == 2 and (S == 4 or S == 1):
            print(Ra)
        if R == 3 and (S == 2 or S == 5):
            print(Ra)
        if R == 4 and (S == 5 or S == 3):
            print(Ra)
        if R == 5 and (S == 1 or S == 2):
            print(Ra)
        if S == 1 and (R == 3 or R == 4):
            print(Sh)
        if S == 2 and (R == 4 or R == 1):
            print(Sh)
        if S == 3 and (R == 2 or R == 5):
            print(Sh)
        if S == 4 and (R == 5 or R == 3):
            print(Sh)
        if S == 5 and (R == 1 or R == 2):
            print(Sh)

