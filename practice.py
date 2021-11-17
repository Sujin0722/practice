import math

n=1000000
a=[True for i in range(n+1)]

for i in range(2, 1001):
    if a[i]:
        for k in range(i+i, n+1, i):
            a[k] = False

while True:
    num = int(input())
    if num == 0: break
    for i in range(3, len(a)):
        if a[i] and a[num-i]:
            print(num, "=", i, "+", num-i)
            break
    else:
        print("Goldbach's conjecture is wrong.")