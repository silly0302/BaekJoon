import sys

arr = [list(map(int, sys.stdin.readline().split()))for _ in range(9)]
max = 0
space = []

for i in range(9):
    for j in range(9):
        if arr[i][j] >= max:
            max = arr[i][j]
            space = [i+1, j+1]
            
print(max)
print(*space)
