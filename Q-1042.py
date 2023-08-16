i= (input()).split()
i = [int(elemento) for elemento in i]
iuns = i.copy()
i.sort()
for it in i:
    print(it)
print()
for it in iuns:
    print(it)