g, d , ge = map(int,input().split())
S = input()

def Grafo(g,d,ge):
    g = g + d*3/2
    g = g + 2.5*ge
    return g

def Dinamica(g,d,ge):
    g = g + 2.5*ge
    d = d + g*2/3
    return d

def Geomtria(g,d,ge):
    g = g + d*3/2
    ge = ge + g*2/5
    #print(ge)
    return ge

if S == "A":
   g = Grafo(g, d ,ge)
   print(int(g))
if S == "B":
    d = Dinamica(g, d, ge)
    print(int(d))
if S == "C":
    ge = Geomtria(g, d, ge)
    print(int(ge))