import sys

que = []
t = int(input())

for i in range(t):
    arr = sys.stdin.readline().split()

    if arr[0] == 'push':
        que.insert(0, arr[1])
    elif arr[0] == 'pop':
        if len(que) != 0:
            print(que.pop())
        else:
            print(-1)
    elif arr[0] == 'size':
        print(len(que))
    elif arr[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif arr[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[len(que)-1])
    elif arr[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])