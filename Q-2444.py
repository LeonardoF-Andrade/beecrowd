vol,n = input().split()
alt = input().split()
vol = int(vol)
for i in range(int(n)):
    vol+= int(alt[i])
    if vol>100:
        vol=100
    elif vol<0:
        vol=0
print(vol)

