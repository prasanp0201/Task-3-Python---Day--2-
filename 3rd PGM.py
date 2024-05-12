#Given a python list [10, 501, 22, 37, ,100,999,87,351]. Find out how many numbers are there in a given python list which are happy numbers

# Function to check if a number is happy
def is_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit)**2 for digit in str(num))
    return num == 1

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Count of happy numbers
happy_count = 0

# Iterate through the numbers and check if they are happy
for num in numbers:
    if is_happy(num):
        happy_count += 1

# Print the count of happy numbers
print("Count of Happy Numbers:", happy_count)