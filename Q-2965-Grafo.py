class Grafo:
    
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]
    
    def add(self, u, v):
        self.grafo[u-1].append(v)

    
    def dfs(self, v): 
        profundidades = []
        for i in self.grafo[v-1]:
            profundidades.extend(self.dfs(i))
        if not profundidades:
            return [(1, [v])]
        max_profundidade = max(profundidades, key=lambda x: x[0])
        print(v, profundidades, self.grafo[v-1])
        print(max_profundidade)
        if max_profundidade[0] == 1: 
         return [(max_profundidade[0] + 1,  self.grafo[v-1][0])]
        else:
            return [(max_profundidade[0] + 1,  v)]

N, K = map(int,input().split())
gra = Grafo(N)
A = list(map(int,input().split()))
for i in range (N-1):
    gra.add(A[i],i+2)

profundidades = {}
a = [0]*(N+1)
b = [0]*(N+1)
for i in range (1,N+1):
    profundidades[i] = gra.dfs(i)

print(profundidades)
"""
a[1] = profundidades[1][0][1]
b[1] = len(profundidades[1][0][1])
for j in range(2, N + 1):
 a[j] = [x for x in profundidades[j][0][1] if x not in profundidades[1][0][1]]
 b[j] = len(a[j])

b.sort(reverse=True)
cont = sum(b[:K])

print(cont)

"""