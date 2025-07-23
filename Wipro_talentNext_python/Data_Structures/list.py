'''1st'''
# Creating a list
my_list = [10, 20, 30, 40, 50]

# Displaying all items
print("List items:", my_list)

# Accessing individual elements
print("First element:", my_list[0])
print("Third element:", my_list[2])

'''2nd'''
my_list.append(60)
print("After appending:", my_list)

'''3rd'''
my_list.reverse()
print("Reversed list:", my_list)

'''4th'''
# Count how many times 30 appears
count = my_list.count(30)
print("Number of occurrences of 30:", count)

'''5th'''
list1 = [1, 2]
list2 = [3, 4]

# Prepending list1 to list2
result = list1 + list2
print("Combined list:", result)

'''6th'''
my_list.insert(1, 99)  # Insert 99 at index 1
print("After insertion:", my_list)

'''7th'''
# Remove item at index 2
del my_list[2]
print("After removing item at index 2:", my_list)

'''8th'''
# Remove first occurrence of 30
my_list.remove(30)
print("After removing first occurrence of 30:", my_list)
