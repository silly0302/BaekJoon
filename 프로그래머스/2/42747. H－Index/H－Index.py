def solution(citations):
    # 인용 횟수를 내림차순으로 정렬
    citations.sort(reverse=True)
    
    # 인덱스와 인용 횟수를 비교해가며 h-index 계산
    for i in range(len(citations)):
        # 논문의 인용 횟수가 현재 인덱스보다 크거나 같다면 h-index 가능성 있음
        if citations[i] <= i:
            return i
    
    # 모든 논문이 h-index보다 많이 인용되었다면, 전체 논문 수가 h-index
    return len(citations)

        