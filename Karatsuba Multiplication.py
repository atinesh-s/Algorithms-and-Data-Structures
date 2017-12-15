# Find the value of multiplication of two n digits numbers by Karatsuba multiplication approach

import math

# Base
B = int(input('Enter the Base: '))

# First Number
n1 = int(input('Enter the first No.: '))

# Second Number
n2 = t = int(input('Enter the Second No.: '))

def karatsuba(n1, n2):
    if (n1 < 10 or n2 < 10):
        return n1 * n2
   
    # log(9)=0.95, log(10)=1, log(99)=1.99, log(100)=2
    # We can choose either n1 or n2 to count no. of digits

    n = math.floor(math.log10(n1)+1)
    n = n // 2
    bn = B ** (n)
        
    x1, x2 = divmod(n1, bn)
    y1, y2 = divmod(n2, bn)

    a = karatsuba(x1, y1)
    c = karatsuba(x2, y2)
    b = karatsuba(x1+x2, y1+y2)-a-c
    tot = a*(B**(2*n)) + b*(B**n) + c

    return tot

res = karatsuba(n1, n2)

print('%d * %d = %d' %(n1, n2, res))