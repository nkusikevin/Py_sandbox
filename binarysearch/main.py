def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage
arr = [2, 5, 7, 9, 12, 15, 18, 20]
target = 9
result = binary_search(arr, target)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")

