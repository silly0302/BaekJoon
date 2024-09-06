def solution(a, b, c, d):

    dice = [a, b, c, d]
    
    from collections import Counter
    count = Counter(dice)
    
    freq = sorted(count.values(), reverse=True)
    numbers = sorted(count.keys())
    
    if freq == [4]:
        return 1111 * numbers[0]
  
    elif freq == [3, 1]:
        p = [k for k, v in count.items() if v == 3][0]
        q = [k for k, v in count.items() if v == 1][0]
        return (10 * p + q) ** 2

    elif freq == [2, 2]:
        p, q = numbers
        return (p + q) * abs(p - q)
  
    elif freq == [2, 1, 1]:
        p = [k for k, v in count.items() if v == 2][0]
        q = [k for k, v in count.items() if v == 1][0]
        r = [k for k, v in count.items() if v == 1 and k != q][0]
        return q * r
    

    elif freq == [1, 1, 1, 1]:
        return min(numbers)
    
    return 0
