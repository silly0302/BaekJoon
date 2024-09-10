def solution(arr):
    c = []
    for i in range(11):
        if 2**i - len(arr) > 0:
            c.append(2**i - len(arr))
        elif 2**i == len(arr):
            break
        if c != []:
            c = sorted(c)
            for j in range(c[0]):
                arr.append(0)
            break  
        
    return arr