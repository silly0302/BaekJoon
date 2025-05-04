import sys

N = int(sys.stdin.readline().strip())

S = str(sys.stdin.readline().strip())
if (len(S) != N):
    print("error")
sumS = 0
for i in range(N):
    sumS += int(S[i])
print(sumS)
    