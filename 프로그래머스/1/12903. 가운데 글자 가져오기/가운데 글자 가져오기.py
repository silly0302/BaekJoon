def solution(s):
    answer = []
    if len(s) % 2 == 1:
        return s[len(s) // 2]
    else:
        answer.append(s[len(s)//2 - 1])
        answer.append(s[len(s)//2])
        return "".join(answer)