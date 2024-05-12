#Give a Python list [10, 501, 22, 37, 100, 999, 87, 351], your task is to create two list one which have all the Even numbers and another list which have all the odd numbers in it 

def separate_even_odd(input_list):
    # Create two lists using list comprehensions
    even_list = [num for num in input_list if num % 2 == 0]
    odd_list = [num for num in input_list if num % 2 != 0]

    return even_list, odd_list

# Given list
input_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Separate even and odd numbers
even_numbers, odd_numbers = separate_even_odd(input_list)

# Print the separated lists
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)