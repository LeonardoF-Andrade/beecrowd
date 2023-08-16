from sys import stdin,stdout
N, K = input().split()
N = int(N)
K = int(K)
mafia= (stdin.readline()).split()
graph = {}

## percorrer ao contrario pelo vetor q ele ja deu e rankear, depois pegar os maiores ranks e percorrer acrescentando os nos visitados q forem ser tirados




for i in range(N-1): 
    print(i)
    if mafia[i] not in graph:
        graph[mafia[i]] = [i+2]
    else:
        graph[mafia[i]].append((i + 2))
    if str(i+2) not in graph:
        graph[str(i+2)] = []

print(graph)
visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def dfs(visited, graph, node,rank ):  #function for dfs 

    if node not in visited:

        print (node)
        visited.append(node)
        for neighbour in graph[str(node)]:
            dfs(visited, graph, str(neighbour))

dfs(visited, graph, '1',1)
print(visited)