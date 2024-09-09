def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        
        if not answer:
            answer.append(arr[i])
            continue
        top = answer[-1]
        if top == arr[i]:
            continue
        else:
            answer.append(arr[i])
    return answer