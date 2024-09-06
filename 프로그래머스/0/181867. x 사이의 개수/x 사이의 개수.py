def solution(myString):
    answer = []
    answer = myString.split('x')
    num = []
    for i in range(len(answer)):
        num.append(len(answer[i]))
    
    return num