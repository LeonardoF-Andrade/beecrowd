import math
N, M, L ,R = list(map(int,input().split()))

def count_ways(N, M, L, R):
    MOD = 10**9 + 7
    count = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == N or j == M:
                if j + L <= M:
                    count += min(M - j + 1, R) - L + 1
                if i + L <= N:
                    count += min(N - i + 1, R) - L + 1
                if i + L <= N and j + L <= M:
                    count += min(min(N - i + 1, M - j + 1), R) - L + 1
                if i + L <= N and j >= L:
                    count += min(min(N - i + 1, j), R) - L + 1
            else:
                if i + L <= N:
                    count += min(N - i + 1, R) - L + 1
    return count % MOD

result = count_ways(N, M, L, R)
print(result)
