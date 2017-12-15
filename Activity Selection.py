# Find the maximum number of completed jobs over a set of jobs, given with start and finish time by Dynamic Programming.

# List of Jobs (<strat_time>, <end_time>) Sorted with <end time>
jobs = [(1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)]

# Total Number of jobs
n = 11

# count
count = 0

# Creating 2-D list of dimension m*n and initialing it to 0
m = [[-float('inf') for x in range(n)] for x in range(n)]

k=0

def Activity_Select(l,h,n):
    if (m[l][h] != -float('inf')):
        return m[l][h]
        
    if (n == 0):
        return 0
        
    q = - float('inf')
    
    k = jobs[l][1]
    for i in range(n):
        if (jobs[i][0] >= k):
            count += 1        
            k = jobs[i][1]
        
    for i in range(n):
        t = Activity_Select(l, i-1, i-l) + Activity_Select(i+1, h, h-i) + 1
        if (t > q):
            q = t;
            m[l][h] = t;
            
    return q
    
res = Activity_Select(0, n-1, n)

print('Maximum %d number of jobs can be completed' %res)