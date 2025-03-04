# Goal: Count the number of contiguous subarrays that sum up to a given value k.

# Brute Force Approach
def number_of_subarrays_with_sum_k_brute(arr, k, n):
    count = 0
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for m in range(i, j + 1):
                sum += arr[m]
            if sum == k:
                count += 1
    return count
# Time Complexity = O(n^3)
# Space Complexity = O(1)

# Better Approach
def number_of_subarrays_with_sum_k_better(arr, k, n):
    count = 0
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum == k:
                count += 1
    return count
# Time Complexity = O(n^2)
# Space Complexity = O(1)

# Optimal Approach
from collections import defaultdict
def number_of_subarrays_with_sum_k_optimal(arr, k, n):
    mpp = defaultdict(int)
    sum = 0
    count = 0
    mpp[0] = 1

    for i in range(n):
        sum += arr[i]
        remove = sum - k
        count += mpp[remove] 
        mpp[sum] += 1       
    return count
# Time Complexity = O(n)
# Space Complexity = O(n)

# User Input
k = int(input("Enter the value of k: "))
n = int(input("Enter the number of elements in the array: "))
user_array = []

for i in range(n):
    element = int(input(f"Enter the element at arr[{i}]: "))
    user_array.append(element)

# result = number_of_subarrays_with_sum_k_brute(user_array, k, n)
# print(result)

# result = number_of_subarrays_with_sum_k_better(user_array, k, n)
# print(result)

result = number_of_subarrays_with_sum_k_optimal(user_array, k, n)
print(result)
