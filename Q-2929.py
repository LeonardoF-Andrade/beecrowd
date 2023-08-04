saco = []

Val = int(input())

def push(saco, grau):
    saco.append(grau)
    
def MIN(saco):
    print(min(saco))

def POP(saco):
    saco.pop()

for i in range(Val):
    A = input().split()
    if A[0] == "PUSH":
        push(saco,int(A[1]))
    elif len(saco) != 0:
        if A[0] == "MIN":
         MIN(saco)
        elif A[0] == "POP":
         POP(saco)
    else: print("EMPTY")