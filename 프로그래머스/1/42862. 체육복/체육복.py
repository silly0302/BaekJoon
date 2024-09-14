def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

   
    for i in range(len(reserve)-1, -1, -1):
        if reserve[i] in lost:
            lost.remove(reserve[i])
            reserve.remove(reserve[i])
    
  
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)

    
    return n - len(lost)

            
    
    