from sys import stdin,stdout
import math
N, K = map(int,stdin.readline().split())
total = N*K
for i in range(1,10):
    passo = math.ceil(round(i*0.1*total,2))
    if i ==9:
        print(passo)
    else:
        print(passo, end=" ")