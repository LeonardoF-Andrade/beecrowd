numsacos, competidores, poppsec = input().split()
sacos = input().split()

sacos = [int(numero) for numero in sacos]
print(sacos)
def dividir_vetor_em_partes(vetor, numero_de_partes):
    tamanho_da_parte = len(vetor) // numero_de_partes
    partes = [vetor[i:i+tamanho_da_parte] for i in range(0, len(vetor), tamanho_da_parte)]
    return partes
print(int(competidores))
partes_divididas = dividir_vetor_em_partes(sacos, int(competidores))
print(partes_divididas)