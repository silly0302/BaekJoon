import sys
N, X = map(int, sys.stdin.readline().strip().split())

A = list(map(int, sys.stdin.readline().strip().split()))
result = ""
for i in A:
    if i < X:
        result += f"{i} "
print(result)