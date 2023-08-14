def verifica(tamanho, area):
    tamanho.sort(reverse = True)
    Cortada = 0
    cm = 0
    aux = tamanho
    while True: 
     print(aux)
     if Cortada == area:
        cm = aux[0]
        break
     else:
        aux3 = aux.count(aux[0])
        if aux.count(aux[0]) <= 2:
         aux[0] = aux[0] - 1
         Cortada += 1
         aux.sort(reverse = True)
        else:
           aux2 = area - Cortada
           aux2 = aux2/aux3
           aux[0] = aux[0] - aux2
           Cortada = area
           
    return cm



while True:
    N, A = map(int,input().split())
    if N == A == 0 :
        break
    tam = list(map(int,input().split()))
    if A == sum(tam):
        print(":D")
    elif A > sum(tam):
        print(A, sum(tam))
    else: 
        cm = verifica(tam,A)
        print(f"{cm:.4f}")
