# Unit 1: Functions — Python Programming

## 1. What Is a Function?

A function is a block of code that performs a specific task. You can create it once and reuse it whenever you need it.

For example, instead of writing the same code repeatedly to display a welcome message, you can create a function and call it whenever necessary.

## 2. Define a Function

In Python, you define a function using the `def` keyword.

```python
def greet():
    print("Hello, welcome to Python!")
```

**Explanation:**

- `def` tells Python that you are creating a function.
- `greet` is the function's name.
- `()` holds any parameters the function may need.
- `:` marks the beginning of the function body.
- The indented line contains the code that runs when the function is called.

## 3. Call a Function

Defining a function does not automatically execute it. You must call the function by writing its name followed by parentheses.

```python
def greet():
    print("Hello, welcome to Python!")

greet()
```

**Output:**

```text
Hello, welcome to Python!
```

## 4. Write Different Functions

You can create multiple functions to perform different tasks.

```python
def add():
    print(10 + 5)

def subtract():
    print(10 - 5)

add()
subtract()
```

**Output:**

```text
15
5
```

Each function performs a separate task, making the program easier to manage and maintain.

## 5. Functions with Parameters

Parameters allow you to pass information into a function.

```python
def greet(name):
    print("Hello", name)

greet("Jonathan")
greet("Peter")
```

**Output:**

```text
Hello Jonathan
Hello Peter
```

Here, `name` is the parameter, while `"Jonathan"` and `"Peter"` are arguments supplied when calling the function.

## 6. Functions That Return Values

The `return` keyword sends a result back to the part of the program that called the function.

```python
def add(a, b):
    return a + b

result = add(10, 5)
print(result)
```

**Output:**

```text
15
```

**Difference between `print()` and `return`:**

- `print()` displays information on the screen.
- `return` sends a value back so that it can be stored, reused, or used in further calculations.

## 7. A Simple Program Using Functions

Here is an example that combines the concepts you have learned.

```python
def calculate_area(length, width):
    return length * width

def display_result(area):
    print("The area of the rectangle is:", area)

length = 10
width = 5

area = calculate_area(length, width)
display_result(area)
```

**Output:**

```text
The area of the rectangle is: 50
```

## 8. Key Takeaways

- **Functions** organise code into reusable blocks.
- **`def`** is used to define a function.
- **Function calls** execute the code inside a function.
- **Parameters and arguments** allow functions to receive information.
- **`return`** allows functions to send results back to the caller.
- **Reusable functions** make programs easier to read, test, debug, and maintain.


