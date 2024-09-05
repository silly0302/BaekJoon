def solution(my_string, overwrite_string, s):
    answer = ""
    tmp = ""
    for i in range(0,s):
        answer += my_string[i]
    a = len(answer)
    b = len(my_string)
    c = len(overwrite_string)
    d = a+c
    
    
    while d < b:
        tmp += my_string[d] 
        d += 1
    answer = answer+overwrite_string+tmp
    return answer


    
        
    
        
    
    
    
