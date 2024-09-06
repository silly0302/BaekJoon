def solution(strArr):
    answer = []
    str = ""
    for i in range(len(strArr)):
        str = strArr[i]
        if i % 2 == 0:
            Th = str.lower()
            answer.append(Th)
        else:
            Eo = str.upper()
            answer.append(Eo)
    return answer