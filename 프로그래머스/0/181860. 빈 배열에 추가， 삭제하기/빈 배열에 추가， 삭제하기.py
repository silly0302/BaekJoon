def solution(arr, flag):
    answer = []
    cnt = 0
    for i in range(len(arr)): 
        if flag[i] == True:
            cnt = 0
            while cnt < arr[i]*2: 
                answer.append(arr[i])
                cnt += 1
            cnt = 0   
        if flag[i] == False:
            cnt = 0
            while cnt < arr[i]:
                answer.pop()
                cnt += 1
            cnt = 0
    return answer