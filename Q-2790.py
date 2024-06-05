import statistics
N = int(input())
d = input().split()
moda2 = statistics.multimode(d)
moda = statistics.mode(d)
modas = len(moda2)
count = [0]* modas
i = 0
j = 0
aux = 1
while True:
  #print(i)
  if d[i] == moda:
    if i == N - 1 and modas > 1 and aux < modas:
       i = -1
       j += 1
       aux += 1
       moda = moda2[j]
    if i == N - 1:
      break
    i = i + 1
    continue
  else:
    if int(moda) + int(d[i]) == 7:
      count[j] += 2
    else:
      count[j] += 1
  if i == N - 1 and modas > 1 and aux < modas:
    i = -1
    j += 1
    aux += 1
    moda = moda2[j]
  if i == N - 1:
    break
  i = i + 1

print(min(count))
