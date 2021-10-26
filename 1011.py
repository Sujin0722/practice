import math
import sys
T = int(input())
count =0
y=0
for i in range(T):
    a,b = map(int, input().split())
    distance = b-a
    x = (math.sqrt(distance))
    if  x % 1 == 0:
        print(int(x*2-1))
    elif distance <=3:
        print(distance)
    else:
        x = math.trunc(x)
        if distance<=x+(x*x):
            print(x*2)
        elif distance>x+(x*x):
            print(x*2+1)
