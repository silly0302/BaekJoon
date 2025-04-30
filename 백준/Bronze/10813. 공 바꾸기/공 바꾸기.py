import sys
N, M = map(int, sys.stdin.readline().strip().split())
a = []
for i in range(N):
    a.append(i+1)

for l in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    ball = a[i-1]
    a[i-1] = a[j-1]
    a[j-1] = ball
    
print(" ".join(map(str, a)))
    