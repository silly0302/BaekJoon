def solution(myString, pat):
    q1 = pat.upper()
    q2 = myString.upper()
    if q1 in q2:
        return 1
    return 0