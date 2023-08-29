n = int(input())
vect = input().split()
vect = list(map(int, vect))
sma = []
ant = 0
indice = 0 
result = sum(vect)
for i in range(n):
    if ant + int(vect[i]) == result/2:
        result = i
        break
    sma.append(ant + int(vect[i]))
    ant += int(vect[i])
print(result+1)