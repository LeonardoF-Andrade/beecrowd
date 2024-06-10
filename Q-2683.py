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

def kruskal(n, edges, reverse=False):


    edges.sort(key=itemgetter(2), reverse=reverse)
   # print(edges)
    #print(aux)
    uf = UnionFind(n)
    mst = 0
    for u, v, w in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst += w
   # print(mst)
    #print(uf.parent)
    return mst


def main():
  C = int(stdin.readline())
  edges = list(tuple(map(int, stdin.readline().split())) for _ in range(C))
    #print(edges)
  mstA = kruskal(C+1, edges, True)
  mstB = kruskal(C+1, edges)

  stdout.write(f"{mstA}\n{mstB}\n")

if __name__ == '__main__':
  main()
