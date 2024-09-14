def solution(people, limit):
    people.sort()  # 무게순으로 정렬
    i, j = 0, len(people) - 1  # 투 포인터 사용
    answer = 0

    while i <= j:
        if people[i] + people[j] <= limit:  # 가장 가벼운 사람과 무거운 사람 태움
            i += 1  # 가벼운 사람 태웠으니 다음 사람으로 이동
        # 무거운 사람은 항상 태워야 하므로 j는 감소
        j -= 1
        answer += 1  # 보트 하나 사용

    return answer

            
   