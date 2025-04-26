import sys

T = int(sys.stdin.readline().strip())
result = []
for i in range(T):
    a, b = map(int, sys.stdin.readline().strip().split())
    result.append(a+b)
    
for i in range(T):
    print(f"Case #{i+1}: {result[i]}")