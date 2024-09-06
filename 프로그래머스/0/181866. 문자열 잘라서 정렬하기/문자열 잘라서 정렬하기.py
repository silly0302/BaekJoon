def solution(myString):
    myString = myString.split('x')
    myString = sorted(myString)
    answer = []
    for i in range(len(myString)):
        if myString[i] == "":
            print("error!")
        else:
            answer.append(myString[i])
        
    return answer