Curu = 300
Boi = 1500
boto = 600
mapin = 1000
iara = 150
Dona = 225
Total = 0

for i in range(0,5):
    valor = int(input())
    if i == 0:
        Total = valor*Curu
    if i == 1:
        Total = valor*Boi + Total
    if i == 2:
        Total = valor*boto + Total
    if i == 3:
        Total = valor*mapin + Total
    if i == 4:
        Total = valor*iara + Total

Total = Total + Dona

print(Total)