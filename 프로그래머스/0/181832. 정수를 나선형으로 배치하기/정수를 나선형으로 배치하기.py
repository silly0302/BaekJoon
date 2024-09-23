def solution(n):
    # n x n 크기의 배열을 0으로 초기화
    arr = [[0] * n for _ in range(n)]
    
    # 초기 값 설정
    num = 1
    x, y = 0, 0  # 시작 위치
    dx, dy = 0, 1  # 처음엔 오른쪽으로 이동
    
    for _ in range(n * n):
        # 현재 위치에 숫자를 채워넣음
        arr[x][y] = num
        num += 1
        
        # 다음 위치 계산
        nx, ny = x + dx, y + dy
        
        # 경계나 이미 숫자가 채워진 칸을 만나면 방향 변경
        if not (0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0):
            # 방향을 오른쪽 → 아래 → 왼쪽 → 위 순으로 변경
            dx, dy = dy, -dx
        

        x, y = x + dx, y + dy
    
    return arr
