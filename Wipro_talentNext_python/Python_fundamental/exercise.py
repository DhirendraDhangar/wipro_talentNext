#Write a program to check if a given number is Positive, Negative, or Zero.
num = int(input('enter the number:'))
if num >0:
    print('positive')
elif num<0:
    print('negative')
else:
    print('zero')

	
#Write a program to check if a given number is odd or even.
n = int(input('enter the number:'))
if n%2==0:
    print('even')
else:
    print('odd')

#Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.
num1 = int(input('enter the number1'))
num2 = int(input('enter the number2'))
def same(num1,num2):
    if num1%10 == num2%10:
        print(True)
    else:
        print(False)

#Write a program to print numbers from 1 to 10 in a single row with one tab space.
for i in range(11):
    print(i,sep=' ')

#Write a program to print even numbers between 23 and 57. Each number should be printed in a separate row.
for i in range(23,58):
    if i%2==0:
        print(i)
#Write a program to check if a given number is prime or not.
def is_prime(n):
    if n<1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True 
numm = int(input('enter the number for prime :'))
if is_prime(numm):
    print(numm , 'is a prime')
else :
    print(numm, 'is not prime')

#Write a program to print prime numbers between 10 and 99.
def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True
#Write a program to print the sum of all the digits of a given number.
number = int(input('enter the number u want the sum of :'))
add = 0 
while number >0 :
    add += number % 10
    number //= 10
print(f'the sum of the digits is:{add}')


    
 #Write a program to reverse a given number and print.
def reverse_(u):
    return int(str(u)[::-1])
nu = int(input('enter the number to reverse:'))
print("reversed number :",reverse_(nu))
 #Write a program to find if the given number is palindrome or not

h = input('enter the number for palindrome:')
p = h[::-1]
if p == h:
    print('palindrome')
else:
    print('not palindrome')