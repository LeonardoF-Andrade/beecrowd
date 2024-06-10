from sys import stdin, stdout
from operator import itemgetter

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

def kruskal(n, edges):

    aux = []
    for i in range(n):
        for j in range(i + 1, n):
            aux.append((i, j, pitagora(edges[i][0], edges[i][1], edges[j][0], edges[j][1])))
            #break
    #print(aux)
    aux.sort(key=itemgetter(2))
    uf = UnionFind(n)
    mst = 0
    for u, v, w in aux:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst += w
   # print(mst)
    #print(uf.parent)
    return mst

def pitagora(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def main():
  C = int(stdin.readline())
  for i in range(C):
    N = int(stdin.readline())
    edges = list(tuple(map(int, stdin.readline().split())) for _ in range(N))
    #print(edges)
    mst = kruskal(N, edges)

    stdout.write(f"{mst / 100.0:.2f}\n")

if __name__ == '__main__':
  main()
