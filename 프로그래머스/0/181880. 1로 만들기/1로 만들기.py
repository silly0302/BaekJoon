def solution(old):
    count = 0
    for i in old:
        while i > 1:  
            if i % 2 == 0:
                i = i // 2
                count = count + 1
            elif i % 2 == 1:
                i = (i-1) // 2
                count = count + 1

    return count