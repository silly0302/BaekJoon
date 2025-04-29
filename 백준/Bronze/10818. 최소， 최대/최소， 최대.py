import sys

N = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))

if len(a) != N:
    print("입력된 숫자 개수가 다릅니다.")
else:
    print(min(a), max(a))
