# Find the maximum sub-array sum by Divide And Conquer (DAC) approach

n = int(input("Enter the size of the list: "))
lst = []
for i in range(n):
	lst.append(int(input("Enter the %d element: " %(i))))

m_left = 0
m_right = 0

def cross_max_Subarray(lst, l, m, h):
    sum = 0
    l_sum = -float('inf')
    for i in range(m, l-1, -1):
        sum += lst[i]
        if (sum > l_sum):
            l_sum = sum
            m_left = i

    sum = 0
    r_sum = -float('inf')
    for i in range(m+1, h+1):
        sum += lst[i]
        if (sum > r_sum):
            r_sum = sum
            m_right = i

    return(m_left, m_right, l_sum+r_sum)

def max_Subarray(lst, l, h):
    if (l == h):
        return(l, h, lst[l])
    else:
        m = (l+h) // 2
        (l_low, l_high, l_sum) = max_Subarray(lst, l, m)
        (r_low, r_high, r_sum) = max_Subarray(lst, m+1, h)
        (c_low, c_high, c_sum) = cross_max_Subarray(lst, l, m, h)

        if (l_sum>=r_sum and l_sum>=c_sum):
            return(l_low, l_high, l_sum)
        elif(r_sum>=l_sum and r_sum>=c_sum):
            return(r_low, r_high, r_sum)
        else:
            return(c_low, c_high, c_sum)

(low, high, max_sum) = max_Subarray(lst, 0, n-1)

print('Maximum Sum = %d from lst[%d]-lst[%d]' %(max_sum, low, high))