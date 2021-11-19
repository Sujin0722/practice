import math
import sys

r= 1000001
flag = 0

arr=[True for _ in range(r)]
for i in range(2, int(math.sqrt(r))):
    if arr[i] == True:
        for j in range(i*2, r, i):
            if arr[j] == True:
                arr[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0: break
    for i in range(3, r):
        if arr[i] and arr[n-i]:
                print("%d = %d + %d"%(n, i, n-i))
                flag = 1
                break
    else:
        print("Goldbach's conjecture is wrong.")