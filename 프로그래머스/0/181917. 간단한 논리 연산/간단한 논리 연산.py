def solution(x1, x2, x3, x4):
    answer = True
    comp1 = True
    comp2 = True
    if x1 or x2 == True:
        comp1 = True
    else:
        comp1 = False
    if x3 or x4 == True:
        comp2 = True
    else:
        comp2 = False
        
    if comp1 and comp2 == True:
        answer = True
    else:
        answer = False
    
    return answer