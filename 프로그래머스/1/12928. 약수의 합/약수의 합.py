def solution(n):
    i = 1
    answer = 0
    while i <= n:
        if n % i == 0:
            answer += i
        i += 1
        
        
    return answer