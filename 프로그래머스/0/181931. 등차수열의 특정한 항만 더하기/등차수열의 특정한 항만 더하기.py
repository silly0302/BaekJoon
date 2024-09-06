def solution(a, d, included):
    answer = 0
    lst = [None] * len(included)
    for i in range(len(included)):
        lst[i] = a + (d*i)
    for i in range(len(included)):
        if included[i] == 1:
            answer = answer + lst[i]
    return answer