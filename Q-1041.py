i= (input()).split()
i[0] = float(i[0])
i[1] = float(i[1])
if i[0] > 0 and i[1] > 0:
    print('Q1')
elif i[0] > 0 and i[1] < 0:
    print('Q4')
elif i[0] < 0 and i[1] > 0:
    print('Q2')
elif i[0] < 0 and i[1] < 0:
    print('Q3')
elif i[0] == 0 and i[1] == 0:
    print('Origem')
elif i[0] == 0:
    print('Eixo Y')
elif i[1] == 0:
    print('Eixo X')