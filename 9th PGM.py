#Given a python list [10,20,30,9] and a value of 59, write a python program to find the triplet in the list whose sum is equal to the given value

def find_triplet_with_sum(nums, target):
    n = len(nums)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == target:
                    return [nums[i], nums[j], nums[k]]
    return None  # Return None if no triplet with the given sum is found

# Example usage:
numbers = [10, 20, 30, 9]
target_sum = 59
triplet = find_triplet_with_sum(numbers, target_sum)

if triplet:
    print(f"Triplet with sum {target_sum} found: {triplet}")
else:
    print(f"No triplet found with sum {target_sum}")