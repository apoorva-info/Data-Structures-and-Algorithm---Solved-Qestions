# Binary Search: A searching algorithm in a limited search space.
# Search in a sorted area

# Goal: Given a sorted array, return the index of a given target value.

# Linear Search
def search_target_linear(arr,n,target):
    for i in range(n):
        if arr[i] == target:
            return i
# Time Complexity = O(n)
# Space Complexity = O(1)

# Search space: Everything between low and high.
def search_target_binary(arr,n,target):
    low = 0 
    high = n - 1
    mid = (low + high)//2
    while low != high != mid:
        if target < arr[mid]:
            high = mid - 1
            mid = (low + high)//2
        elif target > arr[mid]:
            low = mid + 1
            mid = (low + high)//2
    return low


        




    



# User Input
size = int(input(f"Enter the size of the array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
target_value = int(input("Enter the value that you want to search: "))

# Function Call
result = search_target_linear(array,size,target_value)
print(result)
