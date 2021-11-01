import math
import sys

def sosu(num):
    if num == 1: return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

arr = list(range(2, 246912))
sosu_list = []
for i in arr:
    if sosu(i):
        sosu_list.append(i)

while True:
    a = int(input())
    check = 0
    if a == 0:
        break
    for i in sosu_list:
        if a < i <= a*2:
            check += 1
    print(check)