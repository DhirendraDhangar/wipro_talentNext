#Sum of all numbers in a list
def sum_list(numbers):
    return sum(numbers)
print(sum_list([8, 2, 3, 0, 7]))  # Output: 20
#Reverse a string
def reverse_string(text):
    return text[::-1]
print(reverse_string("1234abcd"))  # Output: "dcba4321"
#Factorial of a non-negative integer
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
print(factorial(5))  # Output: 120
#Count uppercase and lowercase letters in a string
def count_case(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)
count_case("Hello World")  # Output: Uppercase: 2, Lowercase: 8
#Print even numbers from a given list
def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]
print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: [2, 4, 6, 8]
#Check whether a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(is_prime(11))  # Output: True