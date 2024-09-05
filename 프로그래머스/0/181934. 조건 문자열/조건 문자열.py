def solution(ineq, eq, n, m):
    answer = 0
    if ineq == ">":
        if eq == "=" and n >=m:
            return 1
        if eq == "!" and n > m:
            return 1
        else:
            return 0
    if ineq == "<":
        
        if eq == "=" and n <=m:
            return 1
        if eq == "!" and n < m:
            return 1
        else:
            return 0
    
            
    return answer