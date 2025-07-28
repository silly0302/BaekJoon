import sys

arr = [list(sys.stdin.readline().strip()) for _ in range(5)]
result = ""

max_len = max(len(row) for row in arr)  # 가장 긴 열 길이


for j in range(max_len):  
    for i in range(5):   
        if j < len(arr[i]):  
            result += arr[i][j]

print(result)
