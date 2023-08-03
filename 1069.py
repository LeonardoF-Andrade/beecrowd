iteracoes = int(input())
for i in range(iteracoes):
    var = input()
    var = var.replace('.','')
    tamanho = len(var)
    aux = var
    while '<>' in aux:
        aux = aux.replace('<>','')
    print(int((len(var)-len(aux))/2))
    
    
                
