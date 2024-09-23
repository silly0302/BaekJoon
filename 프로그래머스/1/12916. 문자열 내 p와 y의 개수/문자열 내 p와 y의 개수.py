def solution(s):
    cmp1 = 0
    cmp2 = 0
    for i in s:
        if i == "p" or i == "P":
            cmp1 += 1
        elif i == "y" or i == "Y":
            cmp2 += 1
    if cmp1 == cmp2:
        return True
    return False
