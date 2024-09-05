def solution(str1, str2):
    m = 0
    x = 0
    n = len(str1)
    answer = []
    for i in range(n*2):
        if i % 2 == 0:
            answer.append(str1[m])
            m = m + 1
        else:
            answer.append(str2[x])
            x = x + 1
        result = "".join(answer)
    return result
