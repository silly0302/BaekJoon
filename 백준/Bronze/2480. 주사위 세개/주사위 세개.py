x, y, z = map(int, input().split())
money = 0
if (x == y == z):
    money = 10000 + (x*1000)
elif x == y  or x == z:
    money = 1000 + (x*100)
elif y == z :
    money = 1000 + (y*100)
else:
    money = max(x,y,z) * 100 
print(money)