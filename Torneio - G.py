n = int(input())
dic = {}
for i in range(n):
    nome,valor = input().split()
    dic[nome] = int(valor)
itera = 0

while True:
    try:
        linha = input()
        if linha == "":
            break
        coisa, coisa2, valor = linha.split()
        if coisa in dic:
            dic[coisa] += coisa2 + '*' + valor + ','
        else:
            dic[coisa] = coisa2 + '*' + valor + ','
    except EOFError:
        break
    itera+=1



def procurar_calcular(vetor,chave):
    if vetor is not None:
        if (not isinstance(vetor, int)) and vetor!='':
            vetor = vetor.split(',')
            vetor.pop()
            for x in range(len(vetor)):
                if vetor[x] != '':
                    indice = vetor[x][0]
                    if not isinstance(dic[indice],int):
                        dic[indice] = procurar_calcular(dic[indice],indice)
                    else:
                        if chave in dic2:
                            dic2[chave] += int(dic[indice])*int(vetor[x][2:])
                        else:
                            dic2[chave] = int(dic[indice])*int(vetor[x][2:])
                        dic[chave] = dic2[chave]
        elif vetor != '':
            return vetor
    
def calculate(dic_aux):
    for indice, (chave, valor) in enumerate(dic.items()):
        procurar_calcular(dic_aux[chave],chave)

dic2={}
calculate(dic)

for chave, valor in dic2.items():
    print(f"{chave} {valor}")


