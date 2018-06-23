# Selection Sort
import random
import time
print "n\ttime"
for k in range(1000,11000,1000):
	a=random.sample(range(10000),k)
	start=time.clock()
	for i in range(len(a)):
		m=i
		for j in range(i+1,len(a)):
			if a[j] < a[m]:
				m=j
		a[i],a[m]=a[m],a[i]
	end=time.clock()
	print k,"\t",(end-start)
