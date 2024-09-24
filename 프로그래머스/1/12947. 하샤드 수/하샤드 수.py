def solution(x):
    lx = list(map(int,str(x)))
    print(lx)
    ha = 0
    for i in lx:
        ha += i
    if x % ha == 0:
        return True
    else:
        return False
        