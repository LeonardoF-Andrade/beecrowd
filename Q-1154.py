med = 0
cont = 0
while True:
    id = int(input()) 
    if id < 0:
        break
    else:
        med = med + id
        cont+=1

print(f"{med/cont:.2f}")

