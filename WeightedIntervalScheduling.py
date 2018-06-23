# WIS_Recursive
jobs = [[0,4,2],[1,6,4],[5,8,4],[2,10,7],[8,11,2],[9,12,1]] # job = [start,time,weight]
jobs = sorted(jobs, key = lambda x: int(x[1]))
print jobs
p = [0]*len(jobs)
for i in range(1,len(jobs)):
    for j in range(i-1,-1,-1):
        if jobs[j][1] <= jobs[i][0]:
            p[i] = j + 1
            break
print p

def WIS_recursive(jobs,p,n = len(jobs)):
    val = OPT(n)
    return val
def OPT(n):
    if n == 0:
        return 0
    return max(OPT(n-1), jobs[n-1][2] + OPT(p[n-1]))
print WIS_recursive(jobs,p)
    
# WIS_Memoization
jobs = [[0,4,2],[1,6,4],[5,8,4],[2,10,7],[8,11,2],[9,12,1]] # job = [start,time,weight]
jobs = sorted(jobs, key = lambda x: int(x[1]))
print jobs
p = [0]*len(jobs)
for i in range(1,len(jobs)):
    for j in range(i-1,-1,-1):
        if jobs[j][1] <= jobs[i][0]:
            p[i] = j + 1
            break
print p

m = [0] + [None]*len(jobs)
def WIS_memoization(jobs,p,n = len(jobs)):
    val = OPT(n)
    return val
def OPT(n):
    if m[n] == None:
        m[n] = max(OPT(n-1), jobs[n-1][2] + OPT(p[n-1]))
    return m[n]
print m
def find_sol(j = len(jobs)):
    if j > 0:
        if jobs[j-1][2] + m[p[j-1]] >= m[j-1]:
            print j,
            find_sol(p[j-1])
        else:
            find_sol(j-1)
print WIS_memoization(jobs,p)
find_sol()

# WIS_Iterative
jobs = [[0,4,2],[1,6,4],[5,8,4],[2,10,7],[8,11,2],[9,12,1]] # job = [start,time,weight]
jobs = sorted(jobs, key = lambda x: int(x[1]))
print jobs
p = [0]*len(jobs)
for i in range(1,len(jobs)):
    for j in range(i-1,-1,-1):
        if jobs[j][1] <= jobs[i][0]:
            p[i] = j + 1
            break
print p

m = [0] + [None]*len(jobs)
def WIS_iterative(jobs,p,n = len(jobs)):
    for i in range(1,n+1):
        m[i] = max(jobs[i-1][2] + m[p[i-1]], m[i-1])
    return m[n]

def find_sol(j = len(jobs)):
    if j > 0:
        if jobs[j-1][2] + m[p[j-1]] >= m[j-1]:
            print j,
            find_sol(p[j-1])
        else:
            find_sol(j-1) 
print WIS_iterative(jobs,p)
find_sol()
