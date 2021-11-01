import sys
# 입력은 1개, 마지막 입력은 0, n~2n
A, B = list(map(int, sys.stdin.readline().split()))
count =0

for tmp in range(A, B+1):
    count = 0
    if tmp>1:
        for i in range(2, int(tmp**0.5)+1):
            if tmp%i == 0:
                count=1
                break
        if count == 0:
            print(tmp)
