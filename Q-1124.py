while True:
    L, C, R, F = input().split()
    if L == "0" and R == "0" and F == "0" and C == "0":
        break
    else:
        R = int(R)
        F = int(F)       
        R = 2*R
        F = 2*F
        L = int(L)
        C = int(C)
        if R+F <= L and (R <= C and F <= C) or R+F <= C and (R <= L and F <= L):
            print("S")
        else: print("N")