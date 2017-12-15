# Coin Changing problem : Identify all possible ways of changing N cent by Greedy Method.
# This is a Naive approach, A simple Memoization can be done to avoid solving same  sub-problem over and over again.

# N
N = 10

# Set of Changes
s = [2, 3, 5, 6]

lst = []

def coin_change_count(C, check):
    # if not empty list, setup a new check list local to function
    if not check:
        check = [0, 0, 0, 0]
        
    for k in range(len(s)):
        if (C == N):
            check = [0, 0, 0, 0]
        i = len(s) - k - 1
        t = C - s[i]
        
        if (t >= 0):
            if (s[i] == 2):
                check[0] += 1
            elif (s[i] == 3):
                check[1] += 1
            elif (s[i] == 5):
                check[2] += 1
            elif (s[i] == 6):
                check[3] += 1
                    
            if (t >= s[0]):
                coin_change_count(t, check)
            
            if (t == 0):
                if (not (check in lst)):
                    lst.append(check)
                    
coin_change_count(N, [0, 0, 0, 0])
print(lst)
print(len(lst))