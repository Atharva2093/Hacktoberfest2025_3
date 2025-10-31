def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# --- Input Logic ---
try:
    nums_str = input("Enter a SORTED list of integers separated by spaces (e.g., 5 10 15 20): ")
    target_str = input("Enter the target integer to search for: ")
    
    nums = [int(x) for x in nums_str.split()]
    target = int(target_str)
    
    index = binary_search(nums, target)
    
    if index != -1:
        print(f"Target {target} found at index: {index}.")
    else:
        print(f"Target {target} was NOT found in the list.")

except ValueError:
    print("Invalid input. Please ensure you enter valid integers only.")
