from sys import stdin,stdout
N, K = input().split()
N = int(N)
K = int(K)
mafia= (stdin.readline()).split()


graph = {}
for i in range(N-1): 
    if mafia[i] not in graph:

        graph[mafia[i]] = [i+2]
    else:
        graph[mafia[i]].append((i + 2))
    print(graph)

print(graph)
visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
    visited.append(node)
    queue.append(node)
    
    while queue:          # Creating loop to visit each node
        m = str(queue.pop(0)) 
        print (m) 
       
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs(visited, graph, '1')