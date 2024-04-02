# Python Documentation

### Task 1: What is a conditional?
A conditional is a statement that performs an action if a certain condition is met.
In Python, conditional statements are written in the form of `if`, `else` and `elif` statements.

Example 1, let's say we have a website that only allows access for people with age 18 and above. We can buid a conditional as follwos:

```python
def age_check(age):
    if age >= 18:
        print("Access granted")
    else:
        print("Access denied, you must be 18 or older")


age_check(17)
```
#### OUTPUT
```python
Access denied, you must be 18 or older
```
The function `age_check(age)` checks if the `age` is greater than or equal to 18 and prints a message accordingly. Here the `else` statement is used to print a message when the condition of age is not met. Note that the action to be performend by the conditional is indented. In python, indentation is used to indicate the scope of a code block.


Example 2: Lets say we want a function to assign grades  base on the marks obtained.

```python
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
```
#### OUTPUT

```python
You have recieved Grade A
```
The function `grade_assign(marks)`, assign grades based on marks obtained. Here the `elif` statement is used to check for multiple conditions and the `else` statement is used when none of the other conditions are met.

### Task 2: What are the different types of loops in Python? Why are they useful?

The two main types of loop in python are the `for` and `while` loops. Loops are mainly used in Python to repeatedly perform an action. Loops allow for automation of tasks in a program and avoid  code repetition.
For example the `for` loop in Python is used to iterate over the elements of a list, array or string and perform a specific action.
The `while` loop on the other hand is used to perform an action until a certain condition is met. `while` loops are specially useful when the exact number of iterations is not known.

Example 1: Lets say we want to print the product of 5 with all the numbers from 5 to 10

```python
def multiplication():

    for num in range(5, 11):
        product = 5 * num
        print(product)


multiplication()
```

#### OUTPUT
```python
25
30
35
40
45
50
```

The `for` loop iterates over the numbers `num` from 5 to 10 and prints the product of 5 and `num`.

Example 2: Suppose we want to print all even numbers smaller than the number we input. A `while` loop can be used to implement this as follows:

```python
def even_number_printer(num):
    i = 1
    while i <= num:
        if i % 2 == 0:
            print(i)
        i += 1


even_number_printer(10)
```
#### OUTPUT
```python
2
4
6
8
10
```
Using `while` loop we can prints all even numbers smaller than `num`. Note that it is important to increment `i` by `1` after each iteration otherwise the while loop will run indefinitely. 

### Task 3: What is a list comprehension in Python?

List comprehension is an easy and compact way to create  new lists based on existing lists in Python. They are a compact way to write loops in python in just a single line of code.

Example 1: Lets say we want to create a list of squares of numbers in a list.


```python
def squares():
    numbers = [num for num in range(1, 11)]
    squares = [number**2 for number in numbers]
    print(numbers)
    print(squares)

squares()
```
#### OUTPUT
```python
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
In the function `squares`, list comprehension is used to first create a list of `numbers` from 1 to 10.Then list comprehension is used again to create a list of `squares` of the numbers in the list `numbers`.


The equivalent code to perform the same task without list comprehension is provided below:
```python
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
```
It can be seen that list comprehansion allows for the same functionality as traditional Python loop but just in one line of code. It enhances readability of the code. 

### Task 4: What is an argument in Python?

In python, argument is a value that is passed to a function whenever it is called. A function can have anywhere between zero to multiple arguments.
For example, the function `squares()` defined in Task 3, example 1 takes zero arguments and prints a list of squares of numbers from 1 to 10. 

Example 1: Now lets define a function that takes 2 arguments and returns their product.

```python
def product(num_1, num_2):
    return num_1 * num_2


print(product(5, 5))
```
#### OUTPUT

```python
25
```
Here `num_1` and `num_2` are the 2 arguments that the `product()` function takes to perform the defined action, in this case multiplication. We can print the product of any two numbers simply by defining the arguments while calling the function as follows: `product(5, 5)`.


Example 2: Now Let's define a function that takes any number of arguments and returns their sum.

```python
def sum_all(*args):
    result = 0
    for arg in args:
        result += arg
    return result


print(sum_all(5, 6, 5))
```

#### OUTPUT

```python
16
```
The function `sum_all(*args)` can any number of arguments `*args` and returns their sum.

Thee are mainly two types of arguments in python: positional and keyword arguments. The function `sum_all` defined above uses positonal arguments i.e. arguments are assigned to the function in the order they are passed. 
We can also use keyword arguments in functions, which follow the following syntax: `'keyword=value'`. Keyword arguments allows the arguments to be passed to a function in any order.
Here is an example of a function that takes multiple types of arguments.

Example 3: Define a function that different types of arguments.

```python
def test_function(num, *args, x=1, y=2, **kwargs):
    print(f"num: {num}, I am a positional argument")
    print(f"args: {args}, I am a collection of positional arguments")
    print(f"x: {x}, I am a keyword argument with a default value of 1")
    print(f"y: {y}, I am a keyword argument with a default value of 1")
    print(f"kwargs: {kwargs}, I am a collection of keyword arguments")


test_function(1, 2, 3, 4, 5, age=12, y=10, name="John")
```

#### OUTPUT
```python
num: 1, I am a positional argument
args: (2, 3, 4, 5), I am a collection of positional arguments
x: 1, I am a keyword argument with a default value of 1
y: 10, I am a keyword argument with a default value of 1
kwargs: {'age': 12, 'name': 'John'}, I am a collection of keyword arguments
```
### Task 5: What is a Lambda function in Python?

In python, a lamda function is an anonymous function that can take any number of arguments but can only have one expression. They are useful when we want to use a simple function only once in the code. The syntax to define a lambda function is as follows: `lambda argument_1, ... : expression `.

Example 1 : Define a lamda function that takes a number and returns its square.

```python
square = lambda x: x**2
print(square(5))
```

#### OUTPUT
```python
25
```

### Task 6: What is a `pip` package?

`pip` is package manager for Python. It can be used to install, update and manage Python packages. 
Packages in Python are collections of reusabe code containing Python functions that perform certain tasks.
For example pip can be used to install packages from the Python Package index (PyPI), which is repository where Python developers share their packages.
The code in these packages can then be reused to perform the specific tasks in our program without the need to write the same code again.
To install a package using `pip` one can simply type the following command: `pip install package_name` in the terminal. 
For Example `numpy` is powerful package that can be used to perform high level mathematical operations in Python.
`pip` can be used to install numpy as follows: `pip install numpy`.
Follwing the installation `numpy` can be imported just like any other module in python by using the `import` command.

Example 1: Once `numpy` has been installed it can be used to create an array and find the mean of the array as follows:

```python
import numpy as np

my_data = np.array([10, 20, 30, 40, 50])
mean = np.mean(my_data)
print(my_data)
print(mean)
```

#### OUTPUT
```python
[10 20 30 40 50]
30.0
```











