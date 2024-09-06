def solution(myString, pat):
    answer = 0
    for i in range(len(myString)):
        subString = myString[:i+1]
        if subString.endswith(pat):
            answer += 1
    return answer