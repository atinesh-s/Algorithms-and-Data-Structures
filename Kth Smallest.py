# Find the kth smallest element of an array by Divide And Conquer (DAC) approach

from random import randint
n = int(input('Enter the size of the list: '))
lst = []
for i in range(n):
	lst.append(int(input('Enter the %d element: ' %(i))))

# kth smallest element to be found
k = int(input('Which smallest element has to be found: '))

def swap(i, j):
    t = lst[i]
    lst[i] = lst[j]
    lst[j] = t

def rand_partition(p, q):
    i = randint(p, q) # i is the pivot position 
    swap(i, q) # Taking pivot to the end of the array
    pivot = lst[q]
    
    k = p
    while (p < q):
        if (lst[p] < pivot):
            swap(p, k)
            k += 1
        p += 1
            
    swap(q, k)
    return k

def select(p, q, k):
    r = rand_partition(p, q)
    t = r - p + 1
    
    if (k == t):
        return lst[r]
    elif (k < t):
        return select(p, r-1, k)
    else:
        return select(r+1, q, k-t)

res = select(0, n-1, k)

print('%dth Smallest Element = %d' %(k, res))