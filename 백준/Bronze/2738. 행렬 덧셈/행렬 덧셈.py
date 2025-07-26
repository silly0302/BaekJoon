import sys

N, M = map(int, sys.stdin.readline().strip().split())
arr1 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr2 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = [[arr1[i][j] + arr2[i][j] for j in range(M)] for i in range(N)]

for row in result:
    print(*row)
        

   
        
        
    