x = int(input())
y = int(input())

Quadrant = [0,0,0,0];

if ( x > 0) :
    Quadrant[0] += 1
    Quadrant[3] += 1
else :
    Quadrant[1] += 1
    Quadrant[2] += 1
    
if ( y > 0 ) :
    Quadrant[0] += 1
    Quadrant[1] += 1
else : 
    Quadrant[2] += 1
    Quadrant[3] += 1
    
print(Quadrant.index(max(Quadrant)) + 1)