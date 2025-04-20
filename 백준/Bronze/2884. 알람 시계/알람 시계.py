hour, min = map(int, input().split())



if (hour > 60 or min > 60 ) :
    print("err")
    
if ( min < 45 ) :
    hour -= 1
    min = 60 - (45 - min)
    if ( hour < 0 ) :
        hour = 23
    print(hour, min)
else :
    print(hour, min-45)