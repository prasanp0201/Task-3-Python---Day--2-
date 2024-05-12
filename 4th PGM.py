#Write a Python program to find the sum of the first and last digit of an integer

def sum_first_last_digit(num):
    # Convert the integer to a string to extract the digits
    num_str = str(num)
    
    # Get the first digit (character) from the string
    first_digit = int(num_str[0])
    
    # Get the last digit (character) from the string
    last_digit = int(num_str[-1])
    
    # Calculate the sum of the first and last digit
    sum_digits = first_digit + last_digit
    
    return sum_digits

# Input an integer from the user
num = int(input("Enter an integer: "))

# Call the function and print the result
result = sum_first_last_digit(num)
print("Sum of the first and last digit:", result)