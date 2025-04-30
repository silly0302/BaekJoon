import sys

N, M = map(int, sys.stdin.readline().strip().split())
a = [0] * N

for l in range(M):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    while i-1 <= j-1:
        a[i-1] = k
        i += 1
print(" ".join(map(str, a)))