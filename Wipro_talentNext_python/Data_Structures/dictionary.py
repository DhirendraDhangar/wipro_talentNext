'''This code snippet demonstrates how to create a dictionary in Python,'''
sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30
print(sample_dict)

'''2nd'''
# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenating dictionaries
result = {}
result.update(dic1)
result.update(dic2)
result.update(dic3)

# Printing the final result
print(result)

'''3rd'''
sample_dict = {1: 'apple', 2: 'banana', 3: 'cherry'}
key_to_check = 2

# Check if the key exists
if key_to_check in sample_dict:
    print("Key exists!")
else:
    print("Key does not exist.")

'''4th'''

sample_dict = {'name': 'Abhishek', 'age': 25, 'city': 'New York'}
print("Keys:")
for key in sample_dict:
    print(key)
print("\nValues:")
for value in sample_dict.values():
    print(value)
print("\nKeys and Values:")
for key, value in sample_dict.items():
    print(f"{key}: {value}")

'''5th'''
squares = {}
for num in range(1, 16):
    squares[num] = num ** 2

print(squares)

'''6th'''
num_dict = {'a': 10, 'b': 20, 'c': 30}
total = sum(num_dict.values())
print("Sum of all values:", total)

