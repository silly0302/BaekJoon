# h-index : 논문 개수(i+1), 피인용 횟수(citations[i]) 둘 중 최솟값

def solution(citations):
    citations.sort(reverse=True)
    print(citations)
    
    for i in range(len(citations)):
        if citations[i] <= i:
            return i
    
    return len(citations)

        