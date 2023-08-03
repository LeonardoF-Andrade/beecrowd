
th = 5

a = int(input())

for i in range(0,a):
    pa = list(input())
    if len(pa) == th:
        print(3)
    else:
        if (pa[0] == "o" and (pa[1] == "n" or pa[2]== "e")) or (pa[1] == "n" and pa[2] == "e"):
            print(1)
        if (pa[0] == "t" and (pa[1] == "w" or pa[2]== "o")) or (pa[1] == "w" and pa[2] == "o"):
            print(2)



