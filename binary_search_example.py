def binary(arr, target):
    # Sort the array to prepare for binary search
    arr.sort()
    print("Sorted array is ->", arr)
    print("Target value is ->", target)
    
    left, right = 0, len(arr) - 1
    
    # Perform binary search on the sorted array
    while left <= right:
        mid = (left + right) // 2
        
        # Check if middle element is the target
        if arr[mid] == target:
            return mid  # Return index in sorted array
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    return -1  # Target not found

# Example usage
arr = [34, 23, 12, 45, 67, 89, 50]
print("Index of target in sorted array:", binary(arr, 50))
