from sys import stdin, stdout, setrecursionlimit
from operator import itemgetter

class Grafo:
    def __init__(self, vertices):
        self.vertices = int(vertices)
        self.height = -1
        self.descen = None
        self.use = False
    def __repr__(self):
        return f"Node({self.vertices}," \
               f" H: {self.height}, " \
               f" N: {self.descen}, " \
               f" {self.use}) "
    def Set(self, height, idi):
        self.height = height
        self.descen = idi  
    def GetUse(self):
        return self.use
    def SetUse(self):
        self.use = True
    def GetHei(self):
        return self.height
    def Getdes(self):
        return self.descen
    

def Height(list, idi):
    global folha
    Path = [(0, None),]
    for i, id in enumerate (list[idi]):
        if i == 0: continue
        print(id)
        Path.append((Height(list, id)+1, id))
    Max = max(Path, key = itemgetter(0))
    list[idi][0].Set(Max[0]+1, Max[1])
    if list[idi][0].descen == None:
        folha+=1
    return Max[0]

def resp(lista, li, j):
    global R, N
    aux = 0
    if lista.GetUse() == False:
        R+=1
        lista.SetUse()
        if lista.descen == None:
            return
        for i in range(j, N):
            if li[i][0].vertices == lista.descen:
                break
        resp(li[i][0],li, j+i)
    return

folha = 0
N, K = map(int,stdin.readline().split())
List , R = [[Grafo(i),] for i in range (0, N+1)], 0
A = stdin.readline().split()
if K >= (N-1):
    print(N)
else:
    for x in map(lambda x: 
                 List[int(x[1])].append(x[0])
                 List[int(x[0])].append(x[1]) i
                 ,
                 enumerate(A, 2)):
        pass

    setrecursionlimit(2**31-2)
    Height(List,1)
    if folha <= K:
        print(N)
    else:
        List = sorted(List, key=lambda x: x[0].GetHei(), reverse=True)
        print(List)
        cont = 0
        for i in range (N):
        
            if List[i][0].use == False:
              if cont == K-1:
                 cont +=1
                 R = R + List[i][0].height 
              else:  
                resp(List[i][0],List,i)
                cont += 1
            if cont == K:
                break
        stdout.write(str(R)+"\n")
