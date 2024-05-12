#Write a python program to find the first non-repeating elements in a given list of integers

def find_first_non_repeating(nums):
    # Dictionary to store frequency of each element
    freq_map = {}
    
    # Iterate through the list to count frequencies
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1
    
    # Iterate through the list again to find the first non-repeating element
    for num in nums:
        if freq_map[num] == 1:
            return num
    
    # If no non-repeating element is found, return None
    return None

# Example usage
numbers = [22, 33, 44, 55, 33, 22, 10, 44, 55]
result = find_first_non_repeating(numbers)

if result is not None:
    print("First non-repeating element:", result)
else:
    print("No non-repeating element found in the list.")