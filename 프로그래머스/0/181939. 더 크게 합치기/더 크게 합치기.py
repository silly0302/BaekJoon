def solution(a, b):

    cmp1 = str(a) + str(b)
    cmp2 = str(b) + str(a)
    
    if int(cmp1) > int(cmp2):
        return int(cmp1)
    else:
        return int(cmp2)
