import math

N = int(input())
tmp=1
i=1

while tmp < N:
    i += 1
    tmp += i

val = tmp - i

if i%2 == 0:
     x = N-val
     y = i-x+1
else:
     x = i - (N-val)+1
     y = N-val

print("%d/%d"%(x,y))




