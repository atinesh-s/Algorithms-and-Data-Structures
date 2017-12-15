# Find the minimum number of scalar multiplication to solve a chain of matrices,  given with dimension by Dynamic Programming method.

# Total no. of Matrcies
n = 6

# Dimension of Matrices
dim = [(30,35), (35,15), (15,5), (5,10), (10,20), (20,25)]

# Creating 2-D list initialized to 0
m = [[0 for x in range(6)] for x in range(6)]
s = [[0 for x in range(6)] for x in range(6)]

for l in range(1, n):
    for i in range(n - l):
        j = i + l
        m[i][j] = float('inf')

        for k in range(i, j):
            t = m[i][k] + m[k+1][j] + (dim[i][0] * dim[k][1] * dim[j][1])
            
            if t < m[i][j]:
                m[i][j] = t
                s[i][j] = k

def print_paren(s, i, j):
    if i == j:
        print('A%d' %i)
    else:
        print('(')
        print_paren(s, i, s[i][j])
        print_paren(s, s[i][j] + 1, j)
        print(')')

print_paren(s, 0, n - 1)