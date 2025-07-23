'''1st'''
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = a / b
    print("Result of division:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integers.")

'''2nd'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

try:
    num = int(input("Enter a number: "))
    print("Prime" if is_prime(num) else "Not a prime")
except ValueError:
    print("Error: Invalid input. Please enter a number.")

'''3rd'''
try:
    filename = input("Enter the filename: ")
    with open(filename, 'r') as file:
        contents = file.read()
        print(contents.title())
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Unexpected error occurred:", e)

'''4th'''
numbers = [10, -5, 12, -1, 0, 23, -7, 8, -3, 2]

try:
    index = int(input("Enter an index (0–9): "))
    num = numbers[index]
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")
except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")