# Task 1:What is a conditional?

# Example if statement in python
def if_statement():
    if 10 > 5:
        print("10 is greater than 5")


# if_statement()


# Example if-else statement in python


def age_check(age):
    if age >= 18:
        print("Access granted")
    else:
        print("Access denied, you must be 18 or older")


# age_check(17)


# Example if-else-elif statement in python


def grade_assign(marks):
    if marks >= 90:
        print("You have received Grade A")
    elif marks >= 80:
        print("You have received Grade B")
    elif marks >= 70:
        print("You have received Grade C")
    elif marks >= 60:
        print("You have received Grade D")
    else:
        print("You have received Grade F")


# grade_assign(92)

# Example nested if-else statement in python


def num_check(num):
    if num > 0:
        print(f" {num} is a positive number")
        if num % 2 == 0:
            print(f" {num} is a positive even number")
        else:
            print(f" {num} is a positive odd number")
    elif num < 0:
        print(f" {num} is a negative number")
    else:
        print(f" {num} is Zero")


# num_check(15)
# num_check(-2)


# Example and or operator in python conditionals
def eligibility_check(age, income):
    if age >= 18 and income >= 50000:
        print("Eligible for loan")
    else:
        print("Not eligible for loan")


# eligibility_check(20, 60000)


# Example or operator in python conditionals
def credential_check(username, email):
    if username == "user" or email == "user@gmail.com":
        print("Enter password")
    else:
        print("Account not found")


# credential_check("user", "user@hotmail.com")


# Example ternary operator in python conditionals
def ternary_operator(num):
    result = "Even" if (num % 2 == 0) else "Odd"
    print(result)


# ternary_operator(5)

# Task 2: Loops in Python

# for loop over a range


def multiplication():
    for num in range(5, 11):
        product = 5 * num
        print(product)


# multiplication()

# for loop over a list


def squared_nums():
    numbers = [5, 2, 3, 8, 9]
    squared = []
    for number in numbers:
        squared.append(number**2)

    print(squared)


# squared_nums()


# Example of while loop
def even_number_printer(num):
    i = 1
    while i <= num:
        if i % 2 == 0:
            print(i)
        i += 1


# even_number_printer(10)


# example of while-else loop
def while_else():
    i = 1
    while i < 6:
        print(i)
        i += 1
    else:
        print("i is no longer less than 6")


# while_else()


# example break
def break_loop():
    count = 0
    while count < 5:
        print("Current count:", count)
        count += 1
        if count == 3:
            break

    print("Out of while loop")


# break_loop()


# example continue
def continue_loop():
    count = 0
    while count < 5:
        count += 1
        if count == 3:
            continue
        print("Current count:", count)

    print("Out of while loop")


# continue_loop()


# Task 3: List Comprehension


def squares():
    numbers = [num for num in range(1, 11)]
    squares = [number**2 for number in numbers]
    print(numbers)
    print(squares)


# squares()


def squares_long():
    numbers = []
    for num in range(1, 11):
        numbers.append(num)
    squares = []
    for number in numbers:
        squares.append(number**2)
    print(numbers)
    print(squares)


# squares_long()

# example of list comprehension filtering


def even_filter(start, end):
    numbers = [num for num in range(start, end) if num % 2 == 0]
    print(numbers)


even_filter(1, 11)


# Task 4: Arguments in Python


# positional
def product(num_1, num_2):
    print(f"{num_1} * {num_2} = {num_1 * num_2}")


# product(5, 10)


# Keyword
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")


# greet(name="Grace", age=25)
# greet(age=25, name="Grace")


# Default
def greet_default(name, age=30):
    print(f"Hello, {name}! You are {age} years old.")


# greet_default("Alice")
# greet_default("Bob", 35)


# Arbitary positional
def sum_all(*args):
    result = 0
    for arg in args:
        result += arg
    return result


# print(sum_all(5, 6, 5))
# print(sum_all(5, 5))


# Arbitary keyword
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# print_info(name="Bruce", age=55, city="Madrid")


def test_function(num, *args, x=1, y=2, **kwargs):
    print(f"num: {num}, I am a positional argument")
    print(f"args: {args}, I am a collection of positional arguments")
    print(f"x: {x}, I am a keyword argument with a default value of 1")
    print(f"y: {y}, I am a keyword argument with a default value of 1")
    print(f"kwargs: {kwargs}, I am a collection of keyword arguments")


# test_function(1, 2, 3, 4, 5, age=12, y=10, name="John")


# Task 5: Lambda Function

square = lambda x: x**2
# print(square(5))


# Task 6: pip install numpy and import numpy

import numpy as np

my_data = np.array([10, 20, 30, 40, 50])
mean = np.mean(my_data)
# print(my_data)
# print(mean)
