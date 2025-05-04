import sys 
T = int(sys.stdin.readline().strip())
a = []
for i in range(T):
    x = str(sys.stdin.readline().strip())
    a.append(x)
for i in range(T):
    print(a[i][0]+a[i][-1])