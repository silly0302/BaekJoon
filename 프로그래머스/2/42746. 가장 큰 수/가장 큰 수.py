def solution(numbers):
    # 숫자들을 문자열로 변환
    numbers = [str(num) for num in numbers]
    
    # 정렬 기준에 따른 비교 함수
    def compare(x, y):
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0

    # 퀵 정렬을 위한 파티션 함수
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if compare(arr[j], pivot) < 0:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    # 퀵 정렬 함수
    def quick_sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort(arr, low, pi - 1)
            quick_sort(arr, pi + 1, high)

    # 정렬 실행
    quick_sort(numbers, 0, len(numbers) - 1)

    # 정렬된 숫자들을 연결해서 결과 문자열 만들기
    answer = ''.join(numbers)
    
    # 결과가 '0'으로만 이루어졌다면 '0'을 반환
    return '0' if answer[0] == '0' else answer
