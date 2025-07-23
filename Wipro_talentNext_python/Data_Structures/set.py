'''1st'''
my_set = {10, 20, 30, 40}
my_set.remove(20)  # Or use my_set.discard(20)
print(my_set)
'''2nd'''
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = set1 & set2  # Or set1.intersection(set2)
print("Intersection:", intersection)
'''3rd'''
set1 = {1, 2}
set2 = {3, 4}
union_set = set1 | set2  # Or set1.union(set2)
print("Union:", union_set)
'''4th'''
my_set = {15, 30, 5, 20}
print("Max:", max(my_set))
print("Min:", min(my_set))
