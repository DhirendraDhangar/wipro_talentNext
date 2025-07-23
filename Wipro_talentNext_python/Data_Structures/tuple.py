'''1st'''
sample_tuple = (5, 10, 15, 20, 25, 30, 35)

# 4th element from first (index 3)
print("4th from first:", sample_tuple[3])

# 4th element from last (index -4)
print("4th from last:", sample_tuple[-4])

'''2nd'''
sample_tuple = ('apple', 'banana', 'cherry')
element = 'banana'

if element in sample_tuple:
    print("Element exists!")
else:
    print("Element does not exist.")

'''3rd'''
sample_list = [1, 2, 3, 4, 5]
converted_tuple = tuple(sample_list)
print("Converted Tuple:", converted_tuple)

'''4th'''
sample_tuple = ('a', 'b', 'c', 'd')
index = sample_tuple.index('c')
print("Index of 'c':", index)

'''5th'''
sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# Replacing last element with 100 in each tuple
updated_list = [(x[0], x[1], 100) for x in sample_list]
print("Updated List:", updated_list)

