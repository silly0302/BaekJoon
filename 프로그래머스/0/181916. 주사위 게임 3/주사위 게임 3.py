def solution(a, b, c, d):
    # 주사위 숫자를 리스트로 수집
    dice = [a, b, c, d]
    
    # 주사위 숫자의 빈도수를 계산
    from collections import Counter
    count = Counter(dice)
    
    # 빈도수 기준으로 정렬
    freq = sorted(count.values(), reverse=True)
    numbers = sorted(count.keys())
    
    # 네 개 모두 같은 경우
    if freq == [4]:
        return 1111 * numbers[0]
    
    # 세 개 같은 경우
    elif freq == [3, 1]:
        p = [k for k, v in count.items() if v == 3][0]
        q = [k for k, v in count.items() if v == 1][0]
        return (10 * p + q) ** 2
    
    # 두 쌍 같은 경우
    elif freq == [2, 2]:
        p, q = numbers
        return (p + q) * abs(p - q)
    
    # 두 개 같은 경우와 다른 두 숫자
    elif freq == [2, 1, 1]:
        p = [k for k, v in count.items() if v == 2][0]
        q = [k for k, v in count.items() if v == 1][0]
        r = [k for k, v in count.items() if v == 1 and k != q][0]
        return q * r
    
    # 모든 숫자가 다른 경우
    elif freq == [1, 1, 1, 1]:
        return min(numbers)
    
    # 이론적으로 여기에 도달하면 안됨
    return 0
