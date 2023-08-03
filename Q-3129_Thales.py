
n = int(input())
album = []
repetidas = []
for i in range(n):
    x = int(input())
    if x in album:
        repetidas.append(x)
    else:
        album.append(x)
print(len(album),"\n",len(repetidas), sep="")