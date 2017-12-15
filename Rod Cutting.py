# You are given a rod of length n, also prices of length 1 to (n− 1) are given.  Use Dynamic Programming to calculate optimal cutting of rod such that profit is maximized.

# Length of Rod
n = 8

# Price of Rod of different Length
p = [1, 5, 8, 9, 10, 17, 17, 20]

r = []
s = []
# since rod of length 0 earns no revenue
r.append(0)

for i in range(n):
    r.append(-float('inf'))# appending 0 also works smarty pants :P

for i in range(n+1):
    s.append(0)

# Use of r in function call is irrelevant
def Cut_Rod_BUE(p, n):
    
    for j in range(1, n+1):
        q = - float('inf')
                
        for i in range(1, j+1):
            if (q < p[i-1] + r[j-i]):          
                q = p[i-1] + r[j-i]
                s[j] = i
        r[j] = q
        
    return r[n]

def Print_Sol(k):
    while (k > 0):
        print(s[k])
        k = k - s[k]
        
res = Cut_Rod_BUE(p, n)

print(res)
print('\n')
Print_Sol(n)