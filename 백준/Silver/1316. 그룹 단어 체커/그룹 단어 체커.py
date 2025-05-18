import sys

N = int(sys.stdin.readline())
s = []
cnt = 0
for i in range(N):
    a = str(sys.stdin.readline())
    for l in range(len(a)):
        if ( l ==  len(a) - 1 and a[l] not in s ) or (l == len(a) - 1 and a[l] == a[l-1]):
            cnt += 1
        elif l != len(a) - 1:
            if a[l] == a[l+1] and a[l] not in s:
                continue
            elif a[l] != a[l+1] and a[l] not in s:
                s.append(a[l])
            else:
                break
    s = []
            
print(cnt)