while True:
    linha = input()
    if linha == "0":
        # Se o usuário pressionar Enter sem digitar nada, saia do loop
        break
    linha = int(linha)
    cont = 0
    for n in range(1,linha+1):
        cont +=n*n
    print(cont)