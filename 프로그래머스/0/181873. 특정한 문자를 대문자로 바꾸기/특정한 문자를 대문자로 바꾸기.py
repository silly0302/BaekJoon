def solution(my_string, alp):
    str_num = 0
    tr = ''
    lst2 = []
    lst = list(my_string)
    for i in lst:
        if i == alp:
            str_num = ord(i) - 32
            lst2.append(chr(str_num))
        else:
            lst2.append(i)
            
            
    return "".join(lst2)