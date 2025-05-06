import sys

T = int(sys.stdin.readline().strip())
a = ""
b = []
for i in range(T):
    R,S = map(str, sys.stdin.readline().strip().split())
    R = int(R)
    for l in range(len(S)):
        a += S[l]*R
    b.append(a)
    a = ""

for i in range(len(b)):
    print(b[i])