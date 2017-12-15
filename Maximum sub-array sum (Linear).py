# Find the maximum sub-array sum by an approach in upper bound of input size n

n = int(input("Enter the size of the list: "))
lst = []
for i in range(n):
	lst.append(int(input("Enter the %d element: " %(i))))

curr_max = max_sofar = 0

for i in lst:
    curr_max = max(0, curr_max + i)
    max_sofar = max(max_sofar, curr_max)
    
print('Maximum Subarray Sum = %d' %max_sofar)