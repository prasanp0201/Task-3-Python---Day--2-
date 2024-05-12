#Given a list of N integers which represents the number of mangoes in a bag. Each bag has a variable number of mangoes. There are M students in Guvi class, task is to distribute mangoes in such a way that each student gets one bag. The difference between the number of mangoes in a bag with maximum mangoes and bag with minimum mangoes given to the student is minimum?


def distribute_mangoes(bags, students):
    # Sort the bags in ascending order
    bags.sort()

    # Calculate the total number of bags required for students
    total_bags = students

    # Initialize variables for maximum and minimum mangoes given to students
    max_mangoes = bags[-1]
    min_mangoes = bags[0]

    # Calculate the difference between max and min mangoes initially
    min_difference = max_mangoes - min_mangoes

    # Initialize index for bag distribution
    bag_index = 0

    # Distribute bags among students in a round-robin fashion
    for i in range(total_bags):
        if bag_index < len(bags):
            max_mangoes = bags[bag_index]
            min_mangoes = bags[i]
            bag_index += 1
            difference = max_mangoes - min_mangoes
            min_difference = min(min_difference, difference)

    return min_difference

# Example usage
bags_list = [5, 10, 101, 77, 55]
students_count = 3
result = distribute_mangoes(bags_list, students_count)
print("Minimum difference between max and min mangoes given to students:", result)