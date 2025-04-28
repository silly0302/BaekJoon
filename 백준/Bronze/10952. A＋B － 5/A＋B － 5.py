import sys
result = []

while True:
    A, B = map(int, sys.stdin.readline().strip().split())
    if (A == 0 and B == 0):
        break
    else: 
        result.append(A + B)
    
for i in range(len(result)):
    if result[i] == 0:
        continue
    print(result[i])