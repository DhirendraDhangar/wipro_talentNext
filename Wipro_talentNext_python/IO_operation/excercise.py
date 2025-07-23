'''1st'''
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

'''2nd'''
n = int(input("Enter the number of lines to read: "))
with open("sample.txt", "r") as file:
    for i in range(n):
        print(file.readline().strip())

'''3rd'''
new_text = input("Enter text to append: ")
with open("sample.txt", "a") as file:
    file.write(new_text + "\n")

'''4th'''
lines = []
with open("sample.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

print(lines)

'''5th'''
with open("sample.txt", "r") as file:
    words = file.read().split()
    longest = max(words, key=len)
    print("Longest word:", longest)

'''6th'''
search_word = input("Enter the word to count: ")
with open("sample.txt", "r") as file:
    words = file.read().split()
    count = words.count(search_word)
    print(f"'{search_word}' appears {count} times.")
