def solution(arr):
    mini = min(arr)  # 최소값을 찾는다
    arr = [x for x in arr if x != mini]  # 최소값을 제외한 새 리스트를 생성한다
    
    if not arr:  # 배열이 비었으면 [-1] 반환
        return [-1]
    
    return arr
