import sys

n = int(input())

if n == 0:
    print(0)
    exit()

arr=''
while n:
    if n%(-2):
        arr = '1'+arr
        n=n//-2+1
    else:
        arr='0'+arr
        n//=-2
print(arr)