N = int(input())
a = []
count = 0
for i in range(N):
  D, T = input().split()
  if count == 0:
    for j in range(len(a)):
      if a[j][0] < D:
        if a[j][1] <= T:
          count = 1;
          break;
      else:
        if a[j][1] >= T:
          count = 1;
          break;
  a.append((D,T));

if count == 0:
  print("S");
else:
  print("N");
