# Python Documentation

### Task 1: What is a conditional?
A conditional is a statement that performs an action if a certain condition is met. They provide a choice for the flow of the program based on the condition, the program’s behavior depends on whether a condition evaluates to `True` (when condition is met) or `False`(when condition is not met). The condition is usually an expression that is tested by the logical operators:
```python
a == b #checks if a equals to b
a != b #checks if not equals to b
a < b #checks if a less than b
a <= b #checks if a less than or equal to b
a > b #checks if a greater than b
a >= b #checks if a greater than or equal to b
```
In Python, conditional statements are written in the form of `if`, `else` and `elif` statements. 

#### `if` Statement
The `if` statement is used when we want to execute a block of code only if a condition holds true. The syntax for writing an `if` statement is as follows:
```python
if condition:
    # Statements to execute if the condition is true
```
 Note that the action to be performed by the conditional is indented. In python, indentation i.e white space at the beginning of the line is used to indicate the scope of a code block. Now let's look at an example of how an `if` conditional can be used in a python code.

```python 
if 10 > 5:
    print("10 is greater than 5")
```

##### OUTPUT

```
10 is greater than 5
```

#### `if-else` Statement
The `if-else` statement combines an additional action (the `else` block) to be executed when the condition is `False`:

```python
if condition:
    # Executes this action if the condition is True
else:
    # Executes this action if the condition is False
```
Let's take a look at an example, let's say we have a website that only allows access for people with age 18 and above. We can build `if-else` conditional as follows:

```python
def age_check(age):
    if age >= 18:
        print("Access granted")
    else:
        print("Access denied, you must be 18 or older")


age_check(17)
```
##### OUTPUT
```
Access denied, you must be 18 or older
```
The function `age_check(age)` checks if the `age` is greater than or equal to 18 and prints a message accordingly. The "Access granted" message is shown if the condition is `True` otherwise the action specified in the `else` block is executed, which in this case will display a "Access denied, you must be 18 or older" message.

#### `elif` Statement
The `elif` statement allows you to check multiple conditions sequentially. As soon as one condition is true, the associated action is executed. As an example Lets say we want a function to assign grades  based on the marks obtained by a student.

```python
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


grade_assign(92)
```
##### OUTPUT

```
You have received Grade A
```
The function `grade_assign(marks)`, assign grades based on marks obtained. Here the `elif` statement is used to check for multiple conditions and the `else` statement is used when none of the other conditions are met.

#### Nested `if-else` Statement
Nested `if-else` statements are useful in Python to check for multiple conditions in a hierarchial manner. Lets say we want to check if a number is positive or negative and only if the number is positive check if it is an even number or an odd number. We can use a nested `if-else` statement to handle this task as follows:

```python 
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


num_check(15)
num_check(-2)
```
##### OUTPUT
```
15 is a positive odd number
-2 is a negative number
```
Here the `num_check(num)` function first checks if the number `num` is either positive, negative or zero and only when the number is positive the code checks wheather the number is odd or even.

#### `and` and `or` operators in Python conditionals
`and` and `or` operators in Python conditionals is used to check for multiple conditions at the same time. The `and` operator yields `TRUE` when both the conditions are met whereas the `or` operator yields `TRUE` when either of the conditions are met. lets look at some examples 
```python 
 def eligibility_check(age, income):
    if age >= 18 and income >= 50000:
        print("Eligible for loan")
    else:
        print("Not eligible for loan")


eligibility_check(20, 60000)
```
##### OUTPUT
```
Eligible for loan
```
The function `eligibility_check()`  prints the message "Eligible for loan" only when both the age and the income entered are above the values provided in the `if` condition. 
```python
# Example or operator in python conditionals
def credential_check(username, email):
    if username == "user" or email == "user@gmail.com":
        print("Enter password")
    else:
        print("Account not found")


credential_check("user", "user@hotmail.com")
```
##### OUTPUT
```
Enter password
```
Whereas, the function `credential_check()`  prints the message "Enter password", when either the username or the email match values provided values in the `if` condition.


#### Ternary operators in Python conditionals
The ternary operator, also known as the conditional expressions, provides a compact way to write conditional statements. It allows us to choose between two values based on a condition. It’s especially useful when you need to assign a value to a variable based on a condition without writing lengthy `if-else` statements. The syntax is as follows:
```python
value_if_true if condition else value_if_false
```
If the condition evaluates to `True`, the expression returns `value_if_true` and if the condition evaluates to `False`, the expression returns `value_if_false`.

Let’s say we want to determine whether a given number is even or odd using the ternary operator. Here’s how we can do it:

```python
def ternary_operator(num):
    result = "Even" if (num % 2 == 0) else "Odd"
    print(result)


ternary_operator(5)
```

##### OUTPUT
```
Odd
```


### Task 2: What are the different types of loops in Python? Why are they useful?

The two main types of loop in python are the `for` and `while` loops. Loops are used in Python to repeatedly perform an action. Loops allow for automation of tasks in a program and helps write efficient code while avoiding  code repetition.


#### `for` loop
The `for` loop in Python is used to iterate over the elements in a list, tuple or other sequences or over the characters in a string and perform a specific action. `for` loops can also be used to execute a block of code a fixed number of times. The basic syntax for executing a  `for` loop in Python is as follows:
```python 
for item in sequence:
    # perform the following action
```
Lets take a look at some examples of `for` loops in Python. For example, let's say we want to print the product of 5 with all the numbers from 5 to 10

```python
def multiplication():

    for num in range(5, 11):
        product = 5 * num
        print(product)


multiplication()
```

##### OUTPUT
```
25
30
35
40
45
50
```

The `for` loop iterates over a range of numbers `num` from 5 to 10 and prints the product of 5 and `num`.

Similarly `for` loops can be used to iterate over a list and perform an action. Lets say we want to iterarate over a list of numbers and perform an operation on each element, we can do that as follows:

```python
def squared_nums():
    numbers = [5, 2, 3, 8, 9]
    squared = []
    for number in numbers:
        squared.append(number**2)

    print(squared)


squared_nums()
```
##### OUTPUT
```
[25, 4, 9, 64, 81]
```
Here the `for` loop iterates over the elements of the `numbers` list and stores the square of each number in the `squared` list.

#### `while` loop
A `while` loop in Python is used to perform an action until a certain condition is met. `while` loops are specially useful when the exact number of iterations is not known in advance. Lets look at an example of a `while` loop. Let's assume we want to print all the even numbers smaller than the number we input. A `while` loop can be used to implement this as follows:

```python
def even_number_printer(num):
    i = 1
    while i <= num:
        if i % 2 == 0:
            print(i)
        i += 1


even_number_printer(10)
```
##### OUTPUT
```
2
4
6
8
10
```
Using `while` loop we can prints all even numbers smaller than `num`. Note that it is important to increment `i` by `1` after each iteration otherwise the while loop will run indefinitely. 

#### `while-else` loop
A `while` loop can also be used in combination with an `else` conditional, where the `else` block will be executed onle the `while` condition is no longer `True`. Let's look at an example

```python
def while_else():
    i = 1
    while i < 6:
        print(i)
        i += 1
    else:
        print("i is no longer less than 6")


while_else()
```
##### OUTPUT
```
1
2
3
4
5
i is no longer less than 6
```

#### `break` and `continue` statements 
`break` and `continue` statements in Python are used to control the flow of loops in Python. they can be used to skip or exit the loop based on a predefined condition. 

`break` statement is used to immediately terminate the execution of the loop even iof the loop comditions are still true. When a `break` condition is encountered in a loop, the loop terminates and the program moves to the next statement outside the loop. Let's look at an example:
```python
def break_loop():
    count = 0
    while count < 5:
        print("Current count:", count)
        count += 1
        if count == 3:
            break

    print("Out of while loop")


break_loop()
```
##### OUTPUT
```
Current count: 0
Current count: 1
Current count: 2
Out of while loop
```

The `continue` statement is used to skip the current iteration of a loop and move to the next iteration. When the `continue` statement is encountered, the current iteration of the loop is terminated, and the program moves to the next iteration. An example is as follows:
```python
def continue_loop():
    count = 0
    while count < 5:
        count += 1
        if count == 3:
            continue
        print("Current count:", count)

    print("Out of while loop")


continue_loop()
```
##### OUTPUT
```
Current count: 1
Current count: 2
Current count: 4
Current count: 5
Out of while loop
```
In this example, the `while` loop skips the iteration when `count` is 3 and continues to the next iteration.
The main difference between `break` and `continue` is that `break` terminates the entire loop, while `continue` skips the current iteration and moves to the next one.


### Task 3: What is a list comprehension in Python?

List comprehension is an easy and compact way to create  new lists based on existing lists in Python. They are a compact way to write loops in python in just a single line of code. The syntax for list comprehension is as follows:
```python 
new_list = [expression for element in old_list]
```
Here, `expression` represents the operation we want to execute on every item within a a list, tuple, or string, 
`element` refers to each value taken from the list, and `old_list` specifies the sequence of elements we want to iterate through.
As example, let's say we want to create a list of squares of numbers in a list.


```python
def squares():
    numbers = [num for num in range(1, 11)]
    squares = [number**2 for number in numbers]
    print(numbers)
    print(squares)

squares()
```
##### OUTPUT
```
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

List comprehension can also be used to filtering some elements in a list to generate a new list. Example:
```python
def even_filter(start, end):
    numbers = [num for num in range(start, end) if num % 2 == 0]
    print(numbers)


even_filter(1, 11)
```
##### OUTPUT
```
[2, 4, 6, 8, 10]
```




### Task 4: What is an argument in Python?

In Python, argument is a value that is passed to a function whenever it is called. It allows the function to operate on that value and perform the desired task. 
A function can be defined to take anywhere between zero to multiple arguments.

#### Types of arguments in Python

#### Positional arguments
These are the most basic type of arguments, where the arguments are passed in the same order as they defined in the function. As an example, lets define a function that takes 2 arguments and returns their product.

```python
def product(num_1, num_2):
    print(f"{num_1} * {num_2} = {num_1 * num_2}")


product(5, 10)
```
##### OUTPUT

```
5 * 10 = 50
```
Here `num_1` and `num_2` are the 2 arguments that the `product()` function takes to perform the defined action, in this case multiplication. We can print the product of any two numbers simply by defining the arguments while calling the function as follows: `product(5, 10)`.

#### Keyword Arguments
Keyword arguments are passed by explicitly naming the parameters they correspond to and the order of the arguments does not matter when using keyword arguments. Example:
```python
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")


greet(name="Grace", age=25)
greet(age=25, name="Grace")
```
##### OUTPUT
```
Hello, Grace! You are 25 years old.
Hello, Grace! You are 25 years old.
```
#### Default Arguments
Default arguments are used to provide a default value for a parameter if no argument is passed when the function is called.
```python
def greet_default(name, age=30):
    print(f"Hello, {name}! You are {age} years old.")


greet_default("Alice")
greet_default("Bob", 35)
```
##### OUTPUT
```
Hello, Alice! You are 30 years old.
Hello, Bob! You are 35 years old.
```
#### Arbitrary positional arguments (`*args`)
This allows you to pass an arbitrary number of positional arguments to a function.
The arguments are collected into a tuple. As an example, let's define a function `sum_all(*args)` that takes any number of arguments `*args` and returns their sum.

```python
def sum_all(*args):
    result = 0
    for arg in args:
        result += arg
    return result


print(sum_all(5, 6, 5))
print(sum_all(5, 5))
```

##### OUTPUT

```
16
10
```

#### Arbitrary keyword arguments (`**kwargs`)
This allows you to pass an arbitrary number of keyword arguments to a function.
The arguments are collected into a dictionary.

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Bruce", age=55, city="Madrid")
```

##### OUTPUT
```
name: Bruce
age: 55
city: Madrid
```
A function can also take multiple types of arguments. For example, let's define a function with different types of arguments.

```python
def test_function(num, *args, x=1, y=2, **kwargs):
    print(f"num: {num}, I am a positional argument")
    print(f"args: {args}, I am a collection of positional arguments")
    print(f"x: {x}, I am a keyword argument with a default value of 1")
    print(f"y: {y}, I am a keyword argument with a default value of 1")
    print(f"kwargs: {kwargs}, I am a collection of keyword arguments")


test_function(1, 2, 3, 4, 5, age=12, y=10, name="John")
```

##### OUTPUT
```
num: 1, I am a positional argument
args: (2, 3, 4, 5), I am a collection of positional arguments
x: 1, I am a keyword argument with a default value of 1
y: 10, I am a keyword argument with a default value of 1
kwargs: {'age': 12, 'name': 'John'}, I am a collection of keyword arguments
```
### Task 5: What is a Lambda function in Python?

In python, a lamda function is an anonymous function that can take any number of arguments but can only have one expression. They are useful when we want to use a simple function only once in the code. The syntax to define a lambda function is as follows: 
```
lambda argument_1, ... : expression
```
Here, `lambda` is the keyword used to define an anonymous function, `argument_1, ..`  are the input parameters for the function, separated by commas and `expression` is a single expression that will be evaluated and returned by the function.

Example 1 : Define a lamda function that takes a number and returns its square.

```python
square = lambda x: x**2
print(square(5))
```

##### OUTPUT
```
25
```

### Task 6: What is a `pip` package?

`pip` is package manager for Python. It can be used to install, update and manage Python packages. 
Packages in Python are collections of reusabe code containing Python functions that perform certain tasks. pip packages are essential for Python development because they provide a wide range of functionality that is not included in the Python standard library. 
For example pip can be used to install packages from the Python Package index (PyPI), which is repository where Python developers can publish and share their packages.
The code in these packages can then be reused to perform the specific tasks in our program without the need to write the same code again. `pip` packages can be easily installed on different operating systems and Python environments, making the code more portable. `pip` also allows to specify the exact version of a package we want to install, ensuring the project always uses a compatible version.
To install a package using `pip` one can simply type the following command: `pip install package_name` in the terminal. 
For Example `numpy` is powerful package that can be used to perform high level mathematical operations in Python. It is a highly used package in Data Science and Machine Learning for data analysis, manipulation and modelling.
`pip` can be used to install numpy as follows: `pip install numpy`.
Follwing the installation `numpy` can be imported just like any other built-in module in python by using the `import` command.

Example 1: Once `numpy` has been installed it can be used to create an array and find the mean of the array as follows:

```python
import numpy as np

my_data = np.array([10, 20, 30, 40, 50])
mean = np.mean(my_data)
print(my_data)
print(mean)
```

##### OUTPUT
```
[10 20 30 40 50]
30.0
```











