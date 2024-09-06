def solution(my_string, m, c):
    answer = []
    for i in range((len(my_string) // m)):
        answer.append(my_string[(m*i)+c-1])
        
    return "".join(answer)