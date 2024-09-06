def solution(arr):
    answer = []
    i = 0
    cnt = 0
    while i < len(arr):
        if answer == []:
            answer.append(arr[i])
            i += 1
        elif answer != [] and answer[cnt] == arr[i]:
            answer.pop()
            i += 1
            if len(answer) >= 1:
                cnt -= 1
        elif answer != [] and answer[cnt] != arr[i]:
            answer.append(arr[i])
            i += 1
            cnt += 1
    if answer == []:
        return [-1]
    return answer