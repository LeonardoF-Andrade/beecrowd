a = input().split()

b = 0
n = int(a[1])
soma_total = (n * (n + 1)) // 2


n = int(a[0]) - 1
soma_subtrair = (n * (n + 1)) // 2
soma_intervalo = soma_total - soma_subtrair
print(soma_intervalo)