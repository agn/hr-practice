#!/usr/local/bin/python2

def diagdiff(arr):
    l2r = []
    r2l = []
    length = len(arr[0]) - 1
    for i in xrange(length + 1):
        l2r.append(arr[i][i])
        r2l.append(arr[i][length - i])

    print l2r, sum(l2r), r2l, sum(r2l)
    return abs(sum(l2r) - sum(r2l))


arr = []

n = int(raw_input())
for i in xrange(n):
    arr.append(map(int, raw_input().rstrip().split()))

print diagdiff(arr)