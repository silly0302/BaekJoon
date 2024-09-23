def solution(arr):
    rows = len(arr)
    cols = len(arr[0])
    
  
    if rows > cols:
        for row in arr:
            row.extend([0] * (rows - cols))  
    
    
    elif cols > rows:
        for _ in range(cols - rows):
            arr.append([0] * cols)  
    
    return arr
