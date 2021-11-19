# 2진수 -> 8진수
import math

n = list((input()))

arr=[]
count = []
if len(n)%3 !=0:
    tmp = len(n)%3
    for i in range(3-tmp):
        n.insert(0, '0')

for i in range(0, len(n), 3):
    arr.append(n[i:i+3])

for c,b,a in arr:
    a=1*int(a)
    b=2*1*int(b)
    c=2*2*int(c)
    count.append(a+b+c)

print(''.join(map(str, count)))