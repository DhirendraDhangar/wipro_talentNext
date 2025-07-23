'''1st - people and fact'''

people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}
print("Initial List:")
for name, fact in people_facts.items():
    print(f"{name}: {fact}")
people_facts["Jeff"] = "Is afraid of heights."
people_facts["Jill"] = "Can hula dance."
print("\nUpdated List:")
for name, fact in people_facts.items():
    print(f"{name}: {fact}")

'''2nd - Find the Runner-Up Score	List'''
scores = [2, 3, 6, 6, 5]
unique_scores = list(set(scores))
unique_scores.sort(reverse=True)
runner_up = unique_scores[1]
print("Runner-up score:", runner_up)

'''3rd	Find the Percentage	Dictionary and List'''
student_marks = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}
name = input("Enter a name: ")
if name in student_marks:
    marks = student_marks[name]
    average = sum(marks) / len(marks)
    print("Average percentage mark:", int(average))
else:
    print("Student not found.")

'''4th	Find the name'''
text = "Hi Alex WelcomeAlex Bye Alex"
name_count = text.count("Alex")

print("Number of times 'Alex' appears:", name_count)
