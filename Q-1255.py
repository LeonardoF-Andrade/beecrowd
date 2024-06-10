from collections import defaultdict
from sys import stdin, stdout

def main():
    N = int(stdin.readline())

    for i in range(N):
        d = defaultdict(int)
        S = stdin.readline().strip()
        for j in S:
            if j.isalpha():
              j = j.lower()
              d[j] += 1
        d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
       # print(d)
        ta = len(d)
        for i in range(ta):
            if d[i] == d[ta-1]:
                stdout.write(d[i][0])
                stdout.write('\n')
                break
            if d[i][1] > d[i+1][1]:
                stdout.write(d[i][0])
                stdout.write('\n')
                break
            else:
                stdout.write(d[i][0])


        #print(d[0][1])


if __name__ == '__main__':
    main()
