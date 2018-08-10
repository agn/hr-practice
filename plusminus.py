#!/usr/local/bin/python2

def plusminus(arr):
    positive = negative = zero = 0
    for i in arr:
        if i == 0:
            zero += 1
        elif i < 0:
            negative += 1
        else:
            positive += 1
    return positive, negative, zero


n = float(raw_input())
arr = map(int, raw_input().rstrip().split())
ptive, ntive, zero = plusminus(arr)
print "{:f}\n{:f}\n{:f}".format(ptive/n, ntive/n, zero/n)