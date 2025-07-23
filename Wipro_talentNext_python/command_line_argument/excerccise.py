'''1st'''
import sys

# sys.argv[1] and sys.argv[2] are the two arguments after the filename
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print("Sum:", num1 + num2)
'''2nd'''
import sys

file_name = sys.argv[0]  # The script filename itself
message = sys.argv[1]    # The welcome message passed

print("File name:", file_name)
print("Welcome message:", message)
'''3rd'''
import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Expects 10 numeric arguments after the filename
numbers = list(map(int, sys.argv[1:11]))  # Takes first 10 arguments
prime_sum = sum(num for num in numbers if is_prime(num))

print("Sum of prime numbers:", prime_sum)
