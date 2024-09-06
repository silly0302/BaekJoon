def solution(arr):
    answer = []
    count = 0
    for i in arr:
        while count < i:
            answer.append(i)
            count += 1
        count = 0
    return answer