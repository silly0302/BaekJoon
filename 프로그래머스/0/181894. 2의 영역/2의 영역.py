def solution(arr):
    answer = []
    start = 0
    end = 0
    n = 0
    for i in range(len(arr)):
        if arr[i] == 2 and n == 0:
            start = i
            n += 1
        elif arr[i] == 2 and n != 0:
            end = i
            n += 1
    if n == 1:
        return [2]
    elif n == 0:
        return [-1]
    else:
        answer = arr[start:end+1]
                
        
    return answer