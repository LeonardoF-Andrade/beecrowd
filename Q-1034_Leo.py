import sys
cont = 0
def calcular_combinacao_minima(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

vetor = list(range(1, 1000000 + 1))
casos = int(sys.stdin.readline().strip())
for _ in range(casos):
    numpedra, tamanho = map(int, sys.stdin.readline().strip().split())
    pedras = list(map(int, sys.stdin.readline().strip().split()))
    pedras.sort()
    min_elementos = calcular_combinacao_minima(pedras, tamanho, [0]*(int(tamanho)+1),[0]*(int(tamanho)+1))
    print(min_elementos)

