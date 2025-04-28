import sys

N = int(sys.stdin.readline().strip())
if N != 0:
    
    find_v = list(map(int, sys.stdin.readline().strip().split()))
    v = int(sys.stdin.readline().strip())
    cnt = 0
    for i in find_v:
        if i == v:
            cnt += 1
print(cnt) 
