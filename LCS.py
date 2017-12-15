# Given two sequences, find the length of Longest Common Sub-sequence (LCS) presents in both of them by Dynamic Programming technique

# Sequences
X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
Y = ['B', 'D', 'C', 'A', 'B', 'A']

# Length of Sequences
m = len(X)
n = len(Y)

# Creating 2-D list of dimension m+1*n+1 and initialing it to 0
c = [[0 for x in range(n+1)] for x in range(m+1)]

# Creating 2-D list of dimension m+1*n+1 and initialing it to 0
b = [[0 for x in range(n+1)] for x in range(m+1)]
   
for i in range(1, m+1):
    for j in range(1, n+1):
        if X[i-1] == Y[j-1]:
            c[i][j] = c[i-1][j-1] + 1
            b[i][j] = 'd'
        elif c[i-1][j] >= c[i][j-1]:
            c[i][j] = c[i-1][j]
            b[i][j] = 'u'
        else:
            c[i][j] = c[i][j-1]
            b[i][j] = 'l'

def print_lcs(i, j):
    if (i == 0 and j == 0) or i == 0 or j == 0:
        return
    if b[i][j] == 'd':
        print_lcs(i-1, j-1)
        print(X[i-1]),
    elif b[i][j] == 'u':
        print_lcs(i-1, j)
    else:
        print_lcs(i, j-1)

# printing LCS
print_lcs(m, n)