from sys import stdin,stdout
N, K = input().split()
N = int(N)
K = int(K)
mafia= (stdin.readline()).split()


graph = {}
for i in range(N-1): 
    print(i)
    if mafia[i] not in graph:
        graph[mafia[i]] = [i+2]
    else:
        graph[mafia[i]].append((i + 2))
    if str(i+2):
        graph[str(i+2)] = []

print(graph)
visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
    visited.append(node)
    queue.append(node)
    
def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, '1')