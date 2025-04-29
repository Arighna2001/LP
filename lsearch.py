# Static array
arr = [5, 8, 12, 15, 20, 25, 30]

# Element to search
target = 15

# Linear Search Algorithm
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where target is found
    return -1  # Return -1 if not found

# Call the function
result = linear_search(arr, target)

# Display result
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
