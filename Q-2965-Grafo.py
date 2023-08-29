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
    def GetHeight(self):
        return self.height   
    def GetUse(self):
        return self.use
    def SetUse(self):
        self.use = True
    

def Height(list, idi):
    Path = [(0, None),]
    for i, id in enumerate (list[idi]):
        if i == 0: continue
        Path.append((Height(list, id)+1, id))
    Max = max(Path, key = itemgetter(0))
    list[idi][0].Set(Max[0]+1, Max[1])
    return Max[0]

N, K = map(int,stdin.readline().split())
List , R = [[Grafo(i),] for i in range (0, N+1)], 0
A = stdin.readline().split()
for x in map(lambda x : List[int(x[1])].append(x[0]), 
         enumerate(A, 2)):
    pass


setrecursionlimit(2**31-2)
Height(List,1)
print(List)
