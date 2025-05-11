good = [1,1,2,2,2,8]

import sys

N = list(map(int, sys.stdin.readline().strip().split()))
a = []
for i in range(len(good)):
    result = good[i] - N[i]
    a.append(result)
    
print((" ".join(map(str,a))))
