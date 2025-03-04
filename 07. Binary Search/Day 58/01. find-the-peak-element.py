# Goal: Find the peak element in a 2D array where the adjacent cells are not same.

# Brute Force Approach
def find_peak_element_brute(arr,m,n):
    for i in range(m):
        for j in range(n):
            up = arr[i - 1][j] if i > 0 else float('-inf')
            down = arr[i + 1][j] if i < m - 1 else float('-inf')
            left = arr[i][j - 1] if j > 0 else float('-inf')
            right = arr[i][j + 1] if j < n - 1 else float('-inf')
            
            if arr[i][j] > max(up, down, left, right):
                return (i, j)  
    return None 
# Time Complexity: O(m*n)
# Space Complexity: O(1)

# Better Approach
def find_peak_element_better(arr, m, n):
    def find_peak_in_column(mid_col):
        max_row = 0
        for i in range(m):
            if arr[i][mid_col] > arr[max_row][mid_col]:
                max_row = i
        return max_row, mid_col
    def search_peak(left_col, right_col):
        if left_col > right_col:
            return None

        mid_col = (left_col + right_col) // 2
        max_row, mid_col = find_peak_in_column(mid_col)

        up = arr[max_row - 1][mid_col] if max_row > 0 else float('-inf')
        down = arr[max_row + 1][mid_col] if max_row < m - 1 else float('-inf')
        left = arr[max_row][mid_col - 1] if mid_col > 0 else float('-inf')
        right = arr[max_row][mid_col + 1] if mid_col < n - 1 else float('-inf')

        if arr[max_row][mid_col] > max(up, down, left, right):
            return (max_row, mid_col)

        if mid_col > 0 and arr[max_row][mid_col - 1] > arr[max_row][mid_col]:
            return search_peak(left_col, mid_col - 1)
        elif mid_col < n - 1 and arr[max_row][mid_col + 1] > arr[max_row][mid_col]:
            return search_peak(mid_col + 1, right_col)
        return None

    return search_peak(0, n - 1)
# Time Complexity: O(m* (log n))
# Space Complexity: O(1)
    
# User Input
import numpy as np
m = int(input("Enter the number of rows in a matrix: "))
n = int(input("Enter the number of columns in a matrix: "))

array = np.empty((m,n), dtype=int)
for i in range(m):
    for j in range(n):
        array[i][j] = int(input(f"Enter the element at array{[i]}{[j]}: "))
print(array)

# Function Call
# result = find_peak_element_brute(array,m,n)
# print(result)
result = find_peak_element_better(array,m,n)
print(result)