def solution(arr, k):
    stck = []
    for i in range(len(arr)):
        if not stck:
            stck.append(arr[i])
            continue
        if arr[i] not in stck:
            stck.append(arr[i])
    result = []
    for i in range(k):
        if i >= len(stck):
            result.append(-1)
        else:
            result.append(stck[i])
        
    return result