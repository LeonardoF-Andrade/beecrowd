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

def pitagora(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def main():
    M, N, K = map(int, stdin.readline().split())
    sensor  = [[0] * 3 for _ in range(K)]
    dist  = [[0] * (K+4) for _ in range(K)]

    for i in range(K):
        aux = list(map(int, stdin.readline().split()))
        sensor[i][0] = aux[0]
        sensor[i][1] = aux[1]
        sensor[i][2] = aux[2]

    #print(sensor[1][1])
   # print (sensor[0])
    #print(dist)
    for i in range(K):
        for j in range(i + 1, K):
            dist[i][j] = pitagora(sensor[i][0], sensor[i][1], sensor[j][0], sensor[j][1])
            dist[j][i] = dist[i][j]


    for i in range(K):
        dist[i][K] = pitagora(sensor[i][0], sensor[i][1], sensor[i][0], 0) #baixo
        dist[i][K+1] = pitagora(sensor[i][0], sensor[i][1], sensor[i][0], N) #cima
        dist[i][K+2] = pitagora(sensor[i][0], sensor[i][1], 0, sensor[i][1]) #esq
        dist[i][K+3] = pitagora(sensor[i][0], sensor[i][1], M ,sensor[i][1]) #dir

    u = UnionFind(K+4)
    for i in range(K):
        for j in range(i+1, K):
            if dist[i][j] <= (sensor[i][2] + sensor[j][2]):
                    u.union(i, j)

    for i in range (K):
        if dist[i][K] <= sensor[i][2]:
            u.union(i, K)
        if dist[i][K+1] <= sensor[i][2]:
            u.union(i, K+1)
        if dist[i][K+2] <= sensor[i][2]:
            u.union(i, K+2)
        if dist[i][K+3] <= sensor[i][2]:
            u.union(i, K+3)


    cont = 0
    for i in range (K):
        if cont >= 1:
             break
        if u.find(i) == u.find(K)  == u.find(K+1):
           # print("aaa")
            cont +=1
        if u.find(i) == u.find(K) == u.find(K+2):
            #print("bbb")
            cont +=1
        if u.find(i) == u.find(K+2) == u.find(K+3):
           # print("ccc")
            cont +=1
        if u.find(i) == u.find(K+3) == u.find(K+1):
            #print("ddd")
            cont +=1

    if cont >= 1:
         stdout.write("N\n")
    else:
         stdout.write("S\n")
    #print(dist)
if __name__ == "__main__":
    main()
