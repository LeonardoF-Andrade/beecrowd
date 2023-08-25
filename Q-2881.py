N = int(input())
show = []
for i in range(N):
    show.append(list(map(int, input().split())))

escolha = []
musicas = 0

def analisa(shows,escolha,musica):
    for i in range (len(shows)):
        for j in range (1,shows[i][0]*3,3):
            if not escolha:
                escolha.append([show[i][j],show[i][j+1],show[i][j+2]])
            else:
                for aux in escolha:
                    if aux:
                        if 


analisa(show,escolha,musicas)
print(escolha)