import sys

while True:
    arr = sys.stdin.readline().rstrip()
    up_cnt, down_cnt, space, num = 0, 0, 0, 0
    if not arr:
        break
    for i in arr:
        if i.isupper():
            up_cnt+=1
        elif i.islower():
            down_cnt+=1
        elif i.isspace():
            space +=1
        elif i.isdigit():
            num+=1
    print("{} {} {} {}".format(down_cnt, up_cnt, num, space))
