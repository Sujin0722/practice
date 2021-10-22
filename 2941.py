arr = (input())
count = 0

n = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in n:
    if i in arr:
        arr = arr.replace(i, '0')

tmp = arr.count('0')
arr = arr.replace('0', '')
print(tmp+len(arr))
