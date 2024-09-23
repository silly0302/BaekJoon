def solution(arr):
    for i in range(len(arr[0])):
        if i == 0:
            continue
        elif arr[0][i] == arr[i][0]:
            continue
        else:
            return 0
    return 1