def solution(n):
    n = list(map(int, str(n)))
    n.sort()
    n.reverse()
    answer = ""
    for i in n:
        answer += str(i)
    return int(answer)
    