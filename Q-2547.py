

while True:
    cont = 0
    try:
        n, mini, maxi = input().split()
    except EOFError:
        break
    
    mini = int(mini)
    maxi = int(maxi)
    n = int(n)
    for n in range(n):
        pessoa = int(input())
        if (pessoa < mini) or (pessoa>maxi):
            cont+=0
        else:
            cont+=1
    
    print(cont)
