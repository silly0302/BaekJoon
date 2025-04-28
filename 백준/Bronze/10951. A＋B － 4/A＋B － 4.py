import sys

while True:
    line = sys.stdin.readline()
    if not line:  # 입력이 없으면 (EOF) 종료
        break
    A, B = map(int, line.strip().split())
    if A == 0 and B == 0:
        break
    print(A + B)
