from sys import stdin, stdout, setrecursionlimit

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.edges[u].append(v)

    def dfs(self, no, rank, visited):
        if visited[no]:
            return
        visited[no] = True
        if no == 0:
            rank[no] = (0,0)
        for v in self.edges[no]:
            rank[v] = (rank[no][0]+1, v)
            self.dfs(v, rank, visited)


    def dfs2(self, no, visited, resp  ,count, aux):
        if visited[no] == True:
            return
        visited[no] = True
        count += 1
        resp[aux] = count

        for v in self.edges[no]:
            self.dfs2(v, visited, resp  ,count, aux)


def main():
    setrecursionlimit(1000000)
    n, k = map(int, stdin.readline().split())
    g = Graph(n)
    g2 = Graph(n)
    for i, v in enumerate(map(int, stdin.readline().split())):
        g2.add_edge(v - 1, i + 1)
        g.add_edge(i + 1, v - 1)
    visited = [False] * (n )
    rank = [(0, 0)] * (n)
    rank[0] = (1, 0)
    g2.dfs(0, rank, visited)

    rank = sorted(rank, key=lambda x: x[0], reverse=True)
    #print(rank)
    visited = [False] * (n)
    resp = [0]*n

    for i in range(n):
        count = 0
        g.dfs2(rank[i][1], visited, resp, count, rank[i][1])

    resp = sorted(resp ,reverse=True)

    solu = 0
    for i in range(k):
      solu += resp[i]

    stdout.write(f"{solu}\n")


if __name__ == '__main__':
    main()
