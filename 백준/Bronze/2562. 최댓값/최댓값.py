list_num = []
for i in range(9):
    x = int(input())
    if x < 0:
        break
    list_num.append(x)
    
print(max(list_num))
print(list_num.index(max(list_num)) + 1)