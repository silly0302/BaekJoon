def solution(my_strings, parts):
    answer = []
    i = 0
    for s,e in parts:
        answer.append(my_strings[i][s:e+1:])
        i += 1
    return "".join(answer)