import sys

t= int(input())
dequeue = []

for i in range(t):
    tmp = sys.stdin.readline().split()

    if tmp[0] == 'push_front':
        dequeue.insert(0, tmp[1])
    elif tmp[0] == 'push_back':
        dequeue.append(tmp[1])
    elif tmp [0] == 'pop_front':
        if len(dequeue) != 0:
            print(dequeue.pop(0))
        else:
            print('-1')
    elif tmp[0] == 'pop_back':
        if len(dequeue) != 0:
            print(dequeue.pop())
        else:
            print('-1')
    elif tmp[0] == 'size':
        print(len(dequeue))
    elif tmp[0] == 'empty':
        if len(dequeue) == 0:
            print('1')
        else:
            print('0')
    elif tmp[0] == 'front':
        if len(dequeue) != 0:
            print(dequeue[0])
        else:
            print('-1')
    elif tmp[0] == 'back':
        if len(dequeue) != 0:
            print(dequeue[len(dequeue)-1])
        else:
            print('-1')