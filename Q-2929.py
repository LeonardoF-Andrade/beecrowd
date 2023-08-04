saco = []

Val = int(input())

def push(saco, grau):
    saco.append(grau)
    
def POP(saco):
    saco.pop()

for i in range(Val):
    A = input().split()
    if A[0] == "PUSH":
        if len(saco) == 0:
           mini = int(A[1])
        else: 
           if int(A[1]) < mini:
              mini = int(A[1])
        push(saco,int(A[1]))
    elif len(saco) != 0:
        if A[0] == "MIN":
         print(mini)
        elif A[0] == "POP":
         POP(saco)
         if len(saco) != 0:
          mini = min(saco)
    else: print("EMPTY")