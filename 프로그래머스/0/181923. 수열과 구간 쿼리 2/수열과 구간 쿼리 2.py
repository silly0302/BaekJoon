def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        mini = float('inf')  
        
        for i in range(s, e + 1):
            if k < arr[i] < mini:
                mini = arr[i]
        
        if mini == float('inf'):
            answer.append(-1)  
        else:
            answer.append(mini)  
    
    return answer
