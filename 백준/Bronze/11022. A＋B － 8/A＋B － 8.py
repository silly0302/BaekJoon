import sys

T = int(sys.stdin.readline().strip())
result = []
A = []
B = []
for i in range(T):
    a, b = map(int, sys.stdin.readline().strip().split())
    result.append(a+b)
    A.append(a)
    B.append(b)
    
for i in range(T):
    print(f"Case #{i+1}: {A[i]} + {B[i]} = {result[i]}")