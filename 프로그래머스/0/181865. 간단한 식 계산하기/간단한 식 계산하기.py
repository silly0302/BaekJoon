def solution(binomial):
    answer = 0
    binomial = binomial.split()
    if '+' in binomial:
        answer = int(binomial[0]) + int(binomial[2])
    elif '-' in binomial:
        answer = int(binomial[0]) - int(binomial[2])
    else:
        answer = int(binomial[0]) * int(binomial[2])
        
        
    return answer