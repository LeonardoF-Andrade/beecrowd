def organiza(A,B,vagao):
    estacao = []
    resposta = []
    cont = 0
    while True:
        for i in range(vagao-1):
            if A[i] == B[cont]:
                resposta.append("I")
                resposta.append("R")
                cont+=1
                A.pop(i)
            else:
                estacao.append(A[i])
                A.pop(i)
        print(estacao)
        break
                


while True:
    vagao = int(input())
    if vagao == 0:
        break
    else:
        A = input().split()
        B = input().split()
        organiza(A,B, vagao)

