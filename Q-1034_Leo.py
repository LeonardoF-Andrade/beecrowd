from functools import lru_cache

cont =0
i = int(input())

@lru_cache(maxsize = 1000000)
def calcula(valores, alvo):
    if alvo == 0:
        return 0
    
    menor_soma = float('inf')
    
    for valor in valores:
        if alvo - int(valor) >= 0:
            soma_atual = calcula(valores, alvo - int(valor)) + 1
            menor_soma = min(menor_soma, soma_atual)
    
    return menor_soma

while cont != i:
    val = 0
    N, M = input().split()
    medidas = input().split()
    medidas.reverse()
    val = calcula(tuple(medidas),int(M))
    print(int(val))
    cont+=1
