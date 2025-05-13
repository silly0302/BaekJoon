import sys

S = str(sys.stdin.readline().strip())
result = 1
for i in range(len(S) // 2):
    if S[i] == S[len(S)-(i+1)]:
        continue
    else:
        result = 0
        break


print(result) 

