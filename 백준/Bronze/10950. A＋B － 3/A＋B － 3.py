n = int(input())
a = []
b = []
for i in range(n):
    x , y = map(int, input().split())
    a.append(x)
    b.append(y)
    
for i in range(n):
    print(a[i] + b[i])