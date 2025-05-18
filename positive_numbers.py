# Program to print all positive numbers in a list

# Example input lists
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

# Using list comprehension to filter positive numbers
positive_list1 = [num for num in list1 if num > 0]
positive_list2 = [num for num in list2 if num > 0]

# Printing the results
print("Input: list1 =", list1)
print("Output:", ', '.join(map(str, positive_list1)))

print("Input: list2 =", list2)
print("Output:", positive_list2)
