def solution(myString):
    myString = list(myString)
    for i in range(len(myString)):
        if ord(myString[i]) < ord('l'):
            myString[i] = 'l'
    
    return "".join(myString)