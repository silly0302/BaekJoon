def solution(l, r):
    result = []
    
    for i in range(l, r + 1):
        num_str = str(i)
        if all(c in '05' for c in num_str):  
            result.append(i)
    
    if not result:  
        return [-1]
    
    return result
