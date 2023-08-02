import Levenshtein

o = "one"
t = "two"
th = 5
lim = 1

a = int(input())

for i in range(0,a):
    pa = input()
    if len(pa) == th:
        print(3)
    else:
        dist1 = Levenshtein.distance(o,pa)
        dist2 = Levenshtein.distance(t,pa)
        if dist1 <= lim:
           print(1)
        elif dist2 <= lim:
           print(2)



