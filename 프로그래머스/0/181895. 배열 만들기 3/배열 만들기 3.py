def solution(arr, intervals):
    answer = []
    num = 0
    for i, j in intervals:
        while i <= j:
            answer.append(arr[i])
            i += 1
            
    return answer