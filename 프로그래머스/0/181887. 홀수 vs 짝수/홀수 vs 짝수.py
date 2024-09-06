def solution(num_list):
    odd = num_list[::2]
    even = num_list[1::2]
    compareod = 0
    compareev = 0
    for i in odd:
        compareod += i
    for i in even:
        compareev += i
    if compareod > compareev:
        return compareod
    else:
        return compareev