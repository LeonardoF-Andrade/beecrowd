


# Abrir o arquivo no modo de leitura
with open('entrada.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Remover o caractere de quebra de linha ('\n') de cada linha
linhas = [linha.strip() for linha in linhas]
dic = {}
iter = int(linhas[0])
linhas = linhas[1:]
for i in range(int(iter)):
    nome,valor = linhas[i].split()
    dic[nome] = int(valor)
linhas = linhas[iter:]
for linha in linhas:
    if linha == "":
        break
    coisa, coisa2, valor = linha.split()
    if coisa in dic:
        dic[coisa] += coisa2 + '*' + valor + ','
    else:
        dic[coisa] = coisa2 + '*' + valor + ','

print(dic)


def procurar_calcular(vetor,chave):
    if vetor is not None:
        if (not isinstance(vetor, int))and vetor!='':
            vetor = vetor.split(',')
            vetor = vetor[:-1]
            print(vetor)
            for x in range(len(vetor)):
                
                indice = vetor[x][0]
                print(indice)
                if not isinstance(dic[indice],int):
                    dic[indice] = procurar_calcular(dic[indice],indice)
                else:
                    if chave in dic2:
                        print(chave)
                        print(dic2[chave])
                        dic2[chave] += int(dic[indice])*int(vetor[x][2:])
                    else:
                        dic2[chave] = int(dic[indice])*int(vetor[x][2:])
                    dic[chave]=dic2[chave]
        elif vetor != '':
            return vetor
    
def calculate(dic_aux):
    for indice, (chave, valor) in enumerate(dic.items()):
        print(dic_aux[chave],chave)
        procurar_calcular(dic_aux[chave],chave)
        

dic2={}
calculate(dic)

for chave, valor in dic2.items():
    print(f"{chave} {valor}")