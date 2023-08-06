
linhas = []
while True:
    entrada = input()
    if entrada == "":
        break  # Se o usuário pressionar Enter, saia do loop
    linhas.append(entrada)


linhas = [linha.strip() for linha in linhas]
dic = {}
iter = int(linhas[0])
linhas = linhas[1:]
for i in range(int(iter)):
    nome,valor = linhas[i].split()
    dic[nome] = valor
linhas = linhas[iter:]
for linha in linhas:
    if linha == "":
        break
    coisa, coisa2, valor = linha.split()
    if coisa in dic:
        dic[coisa] += coisa2 + '*' + valor + ','
    else:
        dic[coisa] = coisa2 + '*' + valor + ','

def verificar_elementos(vetor):
    for elemento in vetor:
        for char in elemento:
            if not (char.isdigit() or char in ['*', '+']):
                return True
    return False
def procurar_calcular(vetor,chave):
    if vetor is not None:
        vetor = vetor.split(',')
        verify = verificar_elementos(vetor)

        if verify:
            for i in range(len(vetor)):
                vet = vetor[i]

                vetor[i] = vet.replace(vet[0],(procurar_calcular((dic[vet[0]]),vet[0])))
            

    

            return '+'.join(vetor)
            
        else:
                return vetor[0]


    
def calculate(dic_aux):
    for indice, (chave, valor) in enumerate(dic.items()):
        if(indice>=iter):
            dic_aux[chave] = str(eval(procurar_calcular(dic_aux[chave][:-1],chave)))
    return dic_aux

dic2={}
dic2 = calculate(dic)

for indice, (chave, valor) in enumerate(dic2.items()):
    if indice>=iter:
        print(f"{chave} {valor}")