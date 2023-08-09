casos = int(input())
primos =[]
twin = []
def is_prime(n):
    if n in primos:
        return True
    i = 2
    while i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        else:
            print(i)
            ##primos.append()
        i += 6

    return True

for caso in range(casos):
    primeiro, ultimo = (input().split())
    primeiro = int(primeiro)
    ultimo=int(ultimo)
    is_prime(ultimo)