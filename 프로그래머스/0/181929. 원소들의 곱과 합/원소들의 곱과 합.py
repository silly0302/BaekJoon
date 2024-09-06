def solution(num_list):
    sum_list = 0
    mult = 0
    for i in range(len(num_list)):
        sum_list += num_list[i]
        if mult == 0:
            mult += num_list[i]
        else:
            mult = mult * num_list[i]
    if mult < sum_list**2:
        return 1
    else:
        return 0