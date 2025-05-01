import sys

N = int(sys.stdin.readline().strip())
x = list(map(int, sys.stdin.readline().strip().split()))
if len(x) != N:
    print("error")
after_x = []
for i in x:
    y = i / max(x) * 100
    after_x.append(y)
    
print(sum(after_x) / len(after_x))