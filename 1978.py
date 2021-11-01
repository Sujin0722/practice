import sys

A= int(sys.stdin.readline())
B = int(sys.stdin.readline())
arr= []
a = []

for i in range(A, B+1):
    count=0
    if i>1:
        for j in range(2,i):
            if i%j == 0:
                count+=1
                break
        if count == 0:
            a.append(i)
if len(a) != 0:
    print(sum(a))
    print(min(a))
else:
    print("-1")