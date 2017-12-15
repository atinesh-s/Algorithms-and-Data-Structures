# Implement Merge Sort

arr = [1,3,5,2,4,6]
n = 6
l = 0
h = n - 1

def merge_Sort(l,h):
    if(l == h):
        return [arr[l]]

    m = (h + l) // 2
    arr1 = merge_Sort(l, m)
    arr2 = merge_Sort(m + 1, h)

    s1 = m - l
    s2 = h - (m + 1)
    mer = []
    k1 = k2 = 0

    while(k1 <= s1 and k2 <= s2):
        if(arr1[k1] < arr2[k2]):
            mer.append(arr1[k1])
            k1 += 1
        else:
            mer.append(arr2[k2])
            k2 += 1

    if(k1 > s1):
        mer.extend(arr2[k2 : s2+1])

    if(k2 > s2):
        mer.extend(arr2[k1 : s1+1])    

    return mer

res=merge_Sort(l, h)

print('Original Array')
print(arr)
print('Sorted Array')
print(res)