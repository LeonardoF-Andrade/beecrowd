saco = []
size = 0

Val = int(input())
 
for i in range(0,Val):
    A = input().split()
    if A[0] == "PUSH":
        saco.append(int(A[1]))
        size+=1
    elif size != 0:
        if A[0] == "MIN":
         print(min(saco))
        elif A[0] == "POP":
         saco.pop(-1)
         size-=1
    else: print("EMPTY")