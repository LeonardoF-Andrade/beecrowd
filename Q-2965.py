def maximum_arrests(N, K, superiors):
    members = {i+2: s for i, s in enumerate(superiors)}
    
    paths = {1: [1]}
    for i in range(2, N+1):
        if i not in members:
            paths[i] = [i]
        else:
            superior = members[i]
            if superior not in paths:
                paths[superior] = [superior]
            paths[i] = [i] + paths[superior]

    
    aux = (paths[N])
    del paths[N]
    cont = 1
    for i in range(N-1,N-K, -1):
        aux = (set(paths[i]) | set(aux))
        cont +=1
    
    return len(aux) +1

N, K = map(int, input().split())
superiors = list(map(int, input().split()))


result = maximum_arrests(N, K, superiors)
print(result)
