import sys

N = int(sys.stdin.readline().strip())

for i in range(N):
    print(" "*(N-(i+1))+"*"*(i+1))