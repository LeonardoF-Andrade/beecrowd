from sys import stdin,stdout
from collections import deque
N, K = input().split()
N = int(N)
K = int(K)
mafia= (stdin.readline()).split()
graph = {}
rank = {}
## percorrer ao contrario pelo vetor q ele ja deu e rankear, depois pegar os maiores ranks e percorrer acrescentando os nos visitados q forem ser tirados

def pegar(k,ranked,visit):
    cont = 0
    for i in range(1,k+1):
        tirar = ranked[-i][0]
        print(tirar)
        indice = tirar-2

        for i in range(K):

    print(visit)
    return cont


for i in range(N-1):
    if int(mafia[i]) not in graph:
        graph[int(mafia[i])] = [i+2]
    else:
        graph[int(mafia[i])].append((i + 2))
    if (i+2) not in graph:
        graph[(i+2)] = []

print(graph)
visited = [] # List for visited nodes.
queue = []     #Initialize a queue
rank = [1]
def dfs(visited, graph, node, num):  #function for dfs

    if node not in visited:
        if(node ==1):
            rank[0] = 1
        else:
            rank.append(num+1)

        print (node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour,num+1)

def bfs(graph, start):
    visited = set()
    queue = deque([(start, 1)])  # Inicializa a fila com o nó de partida e a altura 0
    visited.add(start)

    heights = [[1,1]]  # Dicionário para armazenar as alturas

    while queue:
        node, height = queue.popleft()

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, height + 1))
                heights.append([neighbour,height + 1])  # Armazena a altura do vizinho

    return heights  # Retorna o dicionário de alturas




visited2 = []
rank = bfs(graph, 1)
result = pegar(K,rank,visited2)
print(result)
