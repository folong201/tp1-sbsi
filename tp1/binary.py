def binary_search(sorted_list, target):
    if not sorted_list:
        return -1
    
    left, right = 0, len(sorted_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = sorted_list[mid]
        
        if mid_value == target:
            return mid
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Test cases

if __name__ == "__main__":
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(sorted_list, 5))  # Output: 4
    print(binary_search(sorted_list, 11)) # Output: -1
    print(binary_search([], 1))           # Output: -1

# Time complexity analysis
# Binary search has a time complexity of O(log n) because it divides the search interval in half each time.
# In contrast, a linear search has a time complexity of O(n) because it checks each element one by one.