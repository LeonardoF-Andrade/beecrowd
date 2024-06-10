from sys import stdin, stdout
from operator import itemgetter


def main():
    while True:
      N = stdin.readline()
      try:
          N = int(N)
      except:
         break
      val = [(0, 0)]* N

      for i in range(N):
          val[i] = tuple(map(int, stdin.readline().split()))
      #print(val)
      val.sort(key=itemgetter(1))
      aux = current = 0
      #print(val)

      for i in range (N):
          if val[i][0] > current:
              aux += 1
              current = val[i][1]
      stdout.write(f"{aux}\n")

if __name__ == "__main__":
    main()
