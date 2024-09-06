def solution(arr):
    cnt = 0 
    while True:
        arr2 = []  
        for num in arr:
            if num >= 50 and num % 2 == 0:  
                arr2.append(num // 2)
            elif num < 50 and num % 2 == 1:  
                arr2.append(num * 2 + 1)
            else: 
                arr2.append(num)
        
        if arr == arr2:  
            break
        
        arr = arr2 
        cnt += 1  
    
    return cnt