def solution(n, control):
    answer = n
    lst = [None] * len(control)
    lst = control
    for i in range(len(control)):
        if lst[i] == 'w':
            answer += 1
        elif lst[i] == 's':
            answer -= 1
        elif lst[i] == 'd':
            answer += 10
        elif lst[i] == 'a':
            answer -= 10
    return answer