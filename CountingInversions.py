# Counting Inversions
import random
import time
def merge(a,b):
        m,c = [],0
        if a[0] <= b[0]:
                m.append(a.pop(0))
        else:
                c += len(a)
                m.append(b.pop(0))
        m += a
        m += b
        return m,c
def sort(arr):
        if len(arr) <= 1:
                return arr,0
        mid = len(arr)//2
        b,r1 = sort(arr[:mid])
        c,r2 = sort(arr[mid:])
        d,c = merge(b,c)
        return d,(r1+r2+c)
x = random.sample(range(20),20)
t = time.clock()
s,c = sort(x)
t = time.clock() - t
print "Initial list: ",x
print "Sortred list: ",s
print "Number of Invertions: ",c
print "Time :",t
