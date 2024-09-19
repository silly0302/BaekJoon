def solution(array, commands):
    answer = []
    lst = []
    for l in range(len(commands)):
        i,j,k = commands[l]
        lst = array[i-1:j]
        lst.sort()
        answer.append(lst[k-1])
    return answer
        
    