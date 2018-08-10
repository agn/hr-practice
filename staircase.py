#!/usr/local/bin/python2

def staircase(n):
    for x in range(1,n+1):
        print "{:>{width}}".format('#'*x, width=n)


n = int(raw_input())
staircase(n)