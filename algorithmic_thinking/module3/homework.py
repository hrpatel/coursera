import math

__author__ = 'mamaray'

def mystery(arr, l, r):

    if l > r:
        return -1

    m = int(math.floor((l + r)/2))
    if arr[m] == m:
        return m
    else:
        if arr[m] < m:
            mystery(arr, m+1, r)
        else:
            mystery(arr, l, m-1)

print mystery([-2,0,1,3,7,12,15],0,6)

for i in range(1, 13):
    print range(i), i -1
    print mystery(range(i),0,i-1)
