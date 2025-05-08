import sys

S = sys.stdin.readline().strip()

result = 0
for ch in S:
    if ch in ["W", "X", "Y", "Z"]:
        result += 10
    elif ch in ["T", "U", "V"]:
        result += 9
    elif ch in ["P", "Q", "R", "S"]:
        result += 8
    elif ch in ["M", "N", "O"]:
        result += 7
    elif ch in ["J", "K", "L"]:
        result += 6
    elif ch in ["G", "H", "I"]:
        result += 5
    elif ch in ["D", "E", "F"]:
        result += 4
    elif ch in ["A", "B", "C"]:
        result += 3
print(result)
