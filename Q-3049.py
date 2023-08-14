base_maior = int(input())
base_menor = int(input())
altura = 70
area_e = (base_maior+base_menor)*altura/2

area_t = 70*160

if(area_e>(area_t-area_e)):
    print(1)
elif(area_t-area_e>area_e):
    print(2)
else:
    print(0)