'''1st'''
text = "Hello World"
upper_count = 0
lower_count = 0

for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
'''2nd'''
text = "madam"

cleaned = text.lower().replace(" ", "")
if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
'''3rd'''
text = "Wipro"
n = len(text)
result = text[:2] * n
print(result) 
'''4th'''
text = "xHix"

if text.startswith('x'):
    text = text[1:]
if text.endswith('x'):
    text = text[:-1]

print(text)  # Output: Hi
'''5th'''
text = "Wipro"
n = 3
last_chars = text[-n:]
result = last_chars * n
print(result)  # Output: propropro
