def solution(my_string):
    answer = [0] * 52

    for i in my_string:
        if 'A' <= i <= 'Z':
            num = ord(i)-ord('A')
        elif 'a' <= i <= 'z':
            num = ord(i) - ord('a') + 26
        answer[num] += 1
    return answer