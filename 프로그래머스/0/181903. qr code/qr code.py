def solution(q, r, code):
    result = ''
    for i in range(len(code)):
        if r == i % q:
            result = result + code[i]
    return result