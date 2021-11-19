import math
import sys

n,s=map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))
count =1
tmp = 0

if n==1:
    print(abs(arr[0]-s))
else:
    mod = abs(arr[0]-s)
    for i in range(1, n):
        mod = math.gcd(mod, abs(arr[i]-s))
    print(mod)