from sys import stdin, stdout
from heapq import heappush, heappop

class Heap:
  def __init__(self):
    self.nos = 0
    self.heap = []

  def insert(self, u, indice):
      self.heap.append([u, indice])
      self.nos += 1
      f = self.nos
      while True:
          if f == 1:
              break
          p = f // 2
          if self.heap[p-1][0] <= self.heap[f-1][0]:
              break
          else:
              self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
              f = p

  def remove(self):
      x = self.heap[0]
      self.heap[0] = self.heap[self.nos - 1]
      self.heap.pop()
      self.nos -= 1
      p = 1
      while True:
          f = 2 * p
          if f > self.nos:
              break
          if f + 1 <= self.nos:
              if self.heap[f][0] < self.heap[f-1][0]:
                  f += 1
          if self.heap[p-1][0] <= self.heap[f-1][0]:
              break
          else:
              self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
              p = f
      return x


  def mostra(self):
    print(self.heap)

class Grafo:
  def __init__(self, vertices):
    self.vertices = vertices
    self.grafo = [[0]*vertices for i in range(vertices)]

  def add_aresta(self, u, v, peso):
    self.grafo[u][v] = peso # Unidirecional
    #self.grafo[v][u] = peso  # Bidirecional

  def print_grafo(self):
        for linha in self.grafo:
            print(" ".join(map(str, linha)))

  # Começando de 1 os nós
  def dijkstra(self, origem):
      distancia = [[-1, 0] for i in range(self.vertices)]
      distancia[origem] = [0, origem]
      visitados = [False] * self.vertices
      h = Heap()
      h.insert(0, origem)
      while h.nos > 0:
        d, u = h.remove()
        if visitados[u]:
          continue
        visitados[u] = True
        for v in range(self.vertices):
          if self.grafo[u][v] > 0:
            if distancia[v][0] == -1 or distancia[v][0] >= d + self.grafo[u][v]:
              distancia[v] = [d + self.grafo[u][v], u]
              h.insert(d + self.grafo[u][v], v)
            #  if v+1 == destino:
            #   break
      return distancia


def main():
  C = int(stdin.readline())
  for i in range (C):
    P = int(stdin.readline())
    aux = [''] * P
    aux = list(input().split())  # N -> Quantos nós / M -> Quantas Ligações (Arestas)
   # print(aux[0])
    aux2 = [0]*P
    g = Grafo(P)
    for j in range (P):
      aux2 = list(map(int, input().split()))
      for k in range (P):
        g.add_aresta(j, k, aux2[k])
    #g.print_grafo()
    R = int(stdin.readline())

    for j in range(R):
      partida = 0
      chegada = 0
      aux3 = list(map(str, input().split()))
      partida = aux.index(aux3[1])
      chegada = aux.index(aux3[2])
      resp = g.dijkstra(partida)
      #print(resp)
      caminho = []
      custo = resp[chegada][0]
      caminho.append(aux[chegada])
      auxiliar = chegada
      cont = 0
     # print(resp)
      while True:
        if custo == -1:
            cont +=1
            break
        if resp[auxiliar][0] == -1:
           cont +=1
           break
        aux4 = resp[auxiliar][1]
        caminho.append(aux[aux4])
        auxiliar = aux4
        if aux4 == partida:
          break
      if cont == 0:
        stdout.write(f"Mr {aux3[0]} to go from {aux3[1]} to {aux3[2]}, you will receive {custo} euros\n")
        stdout.write(f"Path:{' '.join(caminho[::-1])}\n")
      else:
         stdout.write(f"Sorry Mr {aux3[0]} you can not go from {aux3[1]} to {aux3[2]}\n")
      #caminho.append(aux[partida])
      #print(" ".join(caminho[::-1]))











    # Rodando para todos os nós como origem
    #for i in range(N):
      #print(g.dijkstra(i+1))

main()
