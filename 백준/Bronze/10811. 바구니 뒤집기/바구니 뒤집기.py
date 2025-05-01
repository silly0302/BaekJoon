import sys

N, M = map(int, sys.stdin.readline().strip().split())

a = [i+1 for i in range(N)] 

for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())

    a[i-1:j] = reversed(a[i-1:j])

print(" ".join(map(str, a)))
