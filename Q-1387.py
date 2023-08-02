while True:
    L, R = list(map(int,input().split()))
    if L == R == 0:
        break
    else:
        print(L+R)