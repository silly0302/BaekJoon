import sys

a = []

for i in range(10):
    N = int(sys.stdin.readline().strip())
    a.append(N % 42)
print(len(set(a)))