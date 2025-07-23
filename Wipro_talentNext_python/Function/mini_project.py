'''Sort the colors	Functions'''
import text_utils

name1 = "bob"
print("Sample Input:", name1)
if text_utils.ispalindrome(name1):
    print("Yes it is a palindrome.")
else:
    print("No it is not a palindrome.")

print("No of vowels:", text_utils.count_the_vowels(name1))

freq = text_utils.frequency_of_letters(name1)
print("Frequency of letters:")
for letter in sorted(freq):
    print(f"{letter}-{freq[letter]}", end=", ")


'''Playing with names'''

def ispalindrome(name):
    if name == name[::-1]:
        print("Yes it is a palindrome.")
    else:
        print("No it is not a palindrome.")

def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in name if char in vowels)
    print("No of vowels:", count)

def frequency_of_letters(name):
    freq = {}
    for char in name:
        freq[char] = freq.get(char, 0) + 1
    
    output = ", ".join([f"{k}-{v}" for k, v in freq.items()])
    print("Frequency of letters:", output)
