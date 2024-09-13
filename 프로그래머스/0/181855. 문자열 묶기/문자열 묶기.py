def solution(strArr):
    answer = []
    cnt = 0
    maxi = 0
    for i in range(len(strArr)):
        answer.append(len(strArr[i]))
    answer = list(sorted(answer))
    an = list(set(answer))
    for i in an:
        if maxi == 0:
            maxi = answer.count(i)
        elif maxi < answer.count(i):
            maxi = answer.count(i)
        else:
            continue
    return maxi
        
        
        