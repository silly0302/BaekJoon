total = int(input())
itemNum = int(input())
result = 0

for _ in range(itemNum):
    itemPrice, cnt = map(int, input().split())
    result += itemPrice * cnt

if total == result:
    print("Yes")
else:
    print("No")
