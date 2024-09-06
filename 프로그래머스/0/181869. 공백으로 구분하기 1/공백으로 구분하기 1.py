def solution(my_string):
    answer = []
    count = 0
    for i in range(len(my_string)):
        if count == 0:
            sub = my_string[:i+1]
        elif count != 0:
            sub = my_string[count:i+1]
        if my_string[i] == ' ':
            sub = my_string[count:i]
            answer.append(sub)
            count = i+1
        if i == len(my_string) - 1:
            answer.append(sub)
        
    return answer