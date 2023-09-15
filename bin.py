def contar_grupos_impares(lista):
    contador = 0  # Inicializa o contador de grupos ímpares
    contagem_temporaria = 0  # Inicializa a contagem temporária de 1s em um grupo

    for elemento in lista:
        if elemento == 1:
            contagem_temporaria += 1
        else:
            # Quando encontramos um 0, verificamos se a contagem temporária é ímpar
            if contagem_temporaria % 2 != 0:
                contador += 1
            contagem_temporaria = 0  # Zera a contagem temporária para o próximo grupo

    # Verifica se o último grupo termina com um número ímpar de 1s
    if contagem_temporaria % 2 != 0:
        contador += 1

    return contador

# Exemplo de uso:
lista = [0, 1, 0]
grupos_impares = contar_grupos_impares(lista)
print(f"{grupos_impares}")
