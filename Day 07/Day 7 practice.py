# Day 7 - Python Practice
# Restored file for the course sequence

# 1) Exception Handling
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Please enter a valid integer.")
else:
    print("No errors occurred.")
finally:
    print("This always executes.")

# 2) List Comprehension
squares = [x * x for x in range(1, 11)]
print("Squares:", squares)

# 3) Lambda and map
nums = [1, 2, 3, 4, 5]
doubles = list(map(lambda n: n * 2, nums))
print("Doubled numbers:", doubles)

# 4) Filter
even_nums = list(filter(lambda n: n % 2 == 0, nums))
print("Even numbers:", even_nums)

# 5) Using functions with default arguments
def greet(name, message="Hello"):
    print(message, name)

greet("Alice")
greet("Bob", "Hi")

# 6) Recursion review

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# 7) Basic challenge
# Write a program to print the sum of all numbers in a list
numbers = [10, 20, 30, 40]
print("Sum:", sum(numbers))

# 8) Practice question
# Create a function to check if a number is prime

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

for x in range(1, 15):
    if is_prime(x):
        print(x, "is prime")
