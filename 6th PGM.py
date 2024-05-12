#You have been given three lists. Task is to find the duplicates in the three lists. Write a python program for the same. You can use your own python lists?

def find_duplicates(list1, list2, list3):
    # Convert lists to sets to remove duplicates
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)

    # Find common elements (duplicates) using set intersection
    duplicates = set1.intersection(set2, set3)

    return list(duplicates)

# Example usage
list1 = [11, 12, 13, 14, 5]
list2 = [33, 14, 55, 5, 100]
list3 = [100, 16, 5, 28, 49]

result = find_duplicates(list1, list2, list3)
print("Duplicates in the three lists:", result)