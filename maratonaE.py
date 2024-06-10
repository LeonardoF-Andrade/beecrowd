from sys import stdin, stdout
from collections import defaultdict

N = int(stdin.readline())
aux = [(0,0)]*N
d = defaultdict(list)

for i in range(N):
  a , b = map(int, stdin.readline().split())
  aux[i] = (a,b)
  d[a].append(b)

for chave in d:
  d[chave].sort()

aux.sort(key=lambda x: x[0])


resp = 0
for i in range(len(d)):
  if len(d[i+1])%2 != 0:
    teste = len(d[i+1])//2
    o = d[i+1][teste]
    for j in range(N):
      a, b = aux[j]
      if a != i+1:
        break
      resp = resp + abs(o-b)
  else:
    teste = len(d[i+1])//2
    o = (d[i+1][teste]+d[i+1][teste-1])/2
    for j in range(N):
      a, b = aux[j]
      if a < i +1:
        continue
      if a != i+1:
        break
      resp = resp + abs(o-b)

stdout.write(f"{int(resp)}\n")
