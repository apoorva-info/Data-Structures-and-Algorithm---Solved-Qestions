# Goal: Given a rotated sorted array with distinct values and a target value, find the index at which target value is present and if not, 
# return -1.

# Linear Search
def linear_search(arr,n,x):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1
#  Time Complexity = O(n)
# Space Complexity = O(1)

def binary_search(arr,n,x):
    low = 0
    high = 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            high = mid + 1
        else:
            low = mid - 1
    return -1

# User Input
size = int(input(f"Enter the size of the sorted array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
x = int(input("Enter the value of the target: "))

# Function Call
# result = linear_search(array,size,x)
# print(result)
result = binary_search(array,size,x)
print(result)