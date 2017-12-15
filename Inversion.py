# Find the inversion of an array by Divide And Conquer (DAC) approach

n = int(input('Enter the size of the list: '))
lst = []
for i in range(n):
	lst.append(int(input('Enter the %d element: ' %(i))))

l = 0
h = n - 1
count = 0

def inversions(l, h):
    if (l == h):
        return [lst[l]]

    m = (h+l) // 2
    lst1 = inversions(l, m)
    lst2 = inversions(m+1, h)

    t1 = s1 = m - l
    s2 = h - (m+1)
    mer = []
    k1 = k2 = 0

    while(k1 <= s1 and k2 <= s2):
        if(lst1[k1] < lst2[k2]):
            mer.append(lst1[k1])
            k1 += 1
            t1 -= 1
        else:
            global count
            count += (t1+1)
            mer.append(lst2[k2])
            k2 += 1

    if (k1 > s1):
        mer.extend(lst2[k2:s2+1])

    if (k2 > s2):
        mer.extend(lst1[k1:s1+1])

    return mer

inversions(l, h)

print('Total No. of Inversions : %d' %count)