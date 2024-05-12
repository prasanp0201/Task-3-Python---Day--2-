#Write a Python program to find the minimum element in rated and sorted list

def find_min_element(sorted_list):
    if not sorted_list:
        return None  # Return None if the list is empty
    
    return sorted_list[0]  # The first element of a sorted list is the minimum element

# Example usage:
sorted_list = [-2, 0, 21, -44, 87]
minimum_element = find_min_element(sorted_list)
print(f"The minimum element in the list is: {minimum_element}")