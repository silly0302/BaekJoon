def solution(a, b):
    answer = 0
    cmp1 = 2 * a * b
    cmp2 = int(f"{a}{b}")
    
    return max(cmp1, cmp2)