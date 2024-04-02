# Task 1:What is a conditional?
def age_check(age):
    if age >= 18:
        print("Access granted")
    else:
        print("Access denied, you must be 18 or older")


age_check(17)


def grade_assign(marks):
    if marks >= 90:
        print("You have recieved Grade A")
    elif marks >= 80:
        print("You have recieved Grade B")
    elif marks >= 70:
        print("You have recieved Grade C")
    elif marks >= 60:
        print("You have recieved Grade D")
    else:
        print("You have recieved Grade F")


grade_assign(92)


# Task 2: Loops in Python


def multiplication():
    for num in range(5, 11):
        product = 5 * num
        print(product)


multiplication()


def even_number_printer(num):
    i = 1
    while i <= num:
        if i % 2 == 0:
            print(i)
        i += 1


even_number_printer(10)

# Task 3: List Comprehension


def squares():
    numbers = [num for num in range(1, 11)]
    squares = [number**2 for number in numbers]
    print(numbers)
    print(squares)


squares()


def squares_long():
    numbers = []
    for num in range(1, 11):
        numbers.append(num)
    squares = []
    for number in numbers:
        squares.append(number**2)
    print(numbers)
    print(squares)


squares_long()


# Task 4: Arguments in Python


def product(num_1, num_2):
    return num_1 * num_2


print(product(5, 5))


def sum_all(*args):
    result = 0
    for arg in args:
        result += arg
    return result


print(sum_all(5, 6, 5))


def test_function(num, *args, x=1, y=2, **kwargs):
    print(f"num: {num}, I am a positional argument")
    print(f"args: {args}, I am a collection of positional arguments")
    print(f"x: {x}, I am a keyword argument with a default value of 1")
    print(f"y: {y}, I am a keyword argument with a default value of 1")
    print(f"kwargs: {kwargs}, I am a collection of keyword arguments")


test_function(1, 2, 3, 4, 5, age=12, y=10, name="John")


# Task 5: Lambda Function

square = lambda x: x**2
print(square(5))


# Task 6: pip install numpy and import numpy

import numpy as np

my_data = np.array([10, 20, 30, 40, 50])
mean = np.mean(my_data)
print(my_data)
print(mean)
