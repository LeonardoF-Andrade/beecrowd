cont = 1


while True:
    c = 0
    d = 0
    ci = 0
    u = 0
    i = int(input())
    if i == 0:
        break

    if i//50 >= 1:
        c = i//50
        i = i%50
    if i//10 >= 1:
        d = i//10
        i = i%10
    if i//5 >= 1:
        ci = i//5
        i = i%5
    if i != 0:
        u = i//1

    print(f"Teste {cont}\n{c} {d} {ci} {u}\n")
    cont += 1