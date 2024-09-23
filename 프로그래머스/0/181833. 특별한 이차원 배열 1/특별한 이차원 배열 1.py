def solution(n):
    # n x n 크기의 2차원 배열을 0으로 초기화
    arr = [[0] * n for _ in range(n)]
    
    # i == j인 위치는 1로 설정
    for i in range(n):
        arr[i][i] = 1
    
    return arr
