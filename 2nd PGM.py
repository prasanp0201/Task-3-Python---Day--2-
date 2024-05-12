#Given a python list [10, 501, 22, 37, ,100,999,87,351], your task is to count all the prime numbers and create a new python list which will contain all the prime numbers in it

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Count of prime numbers and new list of prime numbers
prime_count = 0
prime_numbers = []

# Iterate through the numbers and check if they are prime
for num in numbers:
    if is_prime(num):
        prime_count += 1
        prime_numbers.append(num)

# Print the count of prime numbers and the new list
print("Count of Prime Numbers:", prime_count)
print("Prime Numbers List:", prime_numbers)