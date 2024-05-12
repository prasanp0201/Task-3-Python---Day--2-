#Given a list [4, 2, -3, 1, 6], write a python program to find if there is sublist with sum equal to zero

def has_sublist_with_zero_sum(nums):
    n = len(nums)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum == 0:
                return True
    return False

# Example usage:
numbers = [4, 2, -3, 1, 6]
result = has_sublist_with_zero_sum(numbers)

if result:
    print("Sublist with sum zero exists")
else:
    print("No sublist with sum zero found")