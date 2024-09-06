def solution(myString, pat):
  
    answer =list(myString)
    myString = list(myString)
    for i in range(len(myString)):
        if myString[i] == 'A':
            answer[i] = 'B'
        else:
            answer[i] = 'A'
    answer = "".join(answer)
    if pat in answer:
        return 1
    
    return 0