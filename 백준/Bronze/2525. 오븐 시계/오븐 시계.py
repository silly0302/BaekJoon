hour, min = map(int , input().split())

time = int(input())

min = int(min + time)

if ( min > 59 ) :
    hour += min // 60
    min = min % 60
if (hour > 23) :
    hour = hour % 24
print (hour, min)