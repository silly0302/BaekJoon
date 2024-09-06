def solution(my_string, is_suffix):
    answer = 0
    lst = []
    for i in range(len(my_string)):
        lst.append(my_string[i:])
    for i in range(len(my_string)):
        if is_suffix == lst[i]:
            answer = 1
    return answer