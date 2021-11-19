#최대공약수 GCD / 주어진 정수쌍들의 최대공약수 합

import sys
import math
from itertools import combinations

t = int(input())

def gdc(a, b):
    mod = 2
    cnt=1
    while mod <= int(min(a, b)):
        if a%mod == 0 and b%mod == 0:
            a //= mod
            b //= mod
            cnt *= mod
        else:
            mod+=1
    return cnt

for _ in range(t):
    arr = list(map(int, input().split()))
    combi = list(combinations(arr[1:], 2))
    count = 0
    for a,b in combi:
        count += gdc(a, b)
    print(count)