def solution(myString):
    myString2 = myString.lower()
    list_myString = list(myString2)
    tmp = []
    for i in range(len(list_myString)):
        if list_myString[i] == 'a':
            tmp.append('A')
        else:
            tmp.append(list_myString[i])
    return "".join(tmp)