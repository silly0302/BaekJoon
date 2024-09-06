def solution(my_string, n):
    answer = ''
    list(my_string)
    return "".join(my_string[len(my_string) - n:])