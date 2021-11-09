import sys

arr = list(sys.stdin.readline().rstrip())
abc = 'abcdefghijklmnopqrstuvwxyz'
ABC = abc.upper()
Rot = 13

for i in range(len(arr)):
    if arr[i].isupper():
        point = ord(arr[i]) - ord('A')
        if point+Rot>=26:
            arr[i] = ABC[point+Rot-26]
        else:
            arr[i] = ABC[point+Rot]
    elif arr[i].islower():
        point = ord(arr[i]) - ord('a')
        if point+Rot>=26:
            arr[i] = abc[point+Rot-26]
        else:
            arr[i] = abc[point+Rot]

print("".join(arr))
