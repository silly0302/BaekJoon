def solution(order):
    answer = 0
    for i in range(len(order)):
        if order[i] in ["iceamericano", "americanoice", "hotamericano", "americanohot", "americano", "anything"]:
            answer += 4500
        elif order[i] in ["icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot", "cafelatte"]:
            answer += 5000
    return answer
