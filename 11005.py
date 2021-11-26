n, a = map(int, input().split())
dic = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G',
       17:'H', 18:'I', 19:'J', 20:'K', 21:'L', 22:'M', 23:'N',
       24:'O', 25:'P', 26:'Q', 27:'R', 28:'S', 29:'T', 30:'U',
       31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z'}
arr = ''

while n!=0:
    tmp = n%a
    if tmp>=10:
        arr += dic[tmp]
    else:
        arr += str(tmp)
    n //= a

print(arr[::-1])