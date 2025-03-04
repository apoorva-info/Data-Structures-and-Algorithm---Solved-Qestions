# Goal: To find the median of a row-wise sorted matrix.

# Brute Force Approach
def find_median_brute(arr,m,n):
    ls = []
    for i in range(m):
        for j in range(n):
            ls.append(arr[i][j])
    ls = sorted(ls)
    median = (m * n)//2
    return ls[median]
# Time Complexity: O((m*n)+(m*n)log(m*n))  
# Space Complexity: O(m*n)

# Better Approach 
def blackbox(arr, m, mid):
    count = 0 
    for i in range(m):
        count += upper_bound(arr[i], m, mid)
    return count 
 
def upper_bound(arr,m,x):
    low = 0
    high = m - 1
    ans = m
    while low <= high:
        mid = (low + high)//2
        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans        


def find_median_better(arr, m, n):
    low = float('inf')
    high = float('-inf')
    for i in range(m):
        low = min(low, arr[i][0])
        high = max(high, arr[i][n-1])
    req = (m*n)//2

    while low <= high:
        mid = (low + high)//2
        smaller_equals = blackbox(arr, m, mid)
        if smaller_equals <= req:
            low = mid + 1
        else:
            high = mid - 1
    return low
# Time Complexity: O((log(10^9))*n*log(m))  
# Space Complexity: O(1)

# User Input
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

import numpy as np

array = np.empty((m,n),dtype=int)

for i in range(m):
    for j in range(n):
        array[i][j] = int(input(f"Enter the element at array[{i}][{j}]: "))
print(array)

# Function Call
# result = find_median_brute(array,m,n)
# print(result)
result = find_median_better(array,m,n)
print(result)