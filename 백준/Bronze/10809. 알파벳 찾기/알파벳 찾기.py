import sys

S = str(sys.stdin.readline().strip())
a = []
for i in range(26):
    char = chr(ord('a') + i)
    a.append(S.find(char))
    
    
print(" ".join(map(str, a)))