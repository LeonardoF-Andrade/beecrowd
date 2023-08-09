casos = int(input())
primos =[2,3,5,7,11,13]
twin = []
def is_prime(num):
    if num in primos:
        return True
    if num < primos[-1]:
        return False
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    primos.append(num)
    return True



for caso in range(casos):
    primeiro, ultimo = (input().split())
    primeiro = int(primeiro)
    ultimo=int(ultimo)
    for numero in range(2, ultimo + 1):
        if is_prime(numero):
            indice = primos.index(numero)
        else:
            print(f"{numero} não é um número primo.")
