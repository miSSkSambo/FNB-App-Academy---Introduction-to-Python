# Function Summative Test Quiz

## Chapter 1: Python Functions

## Overview

This summative test assesses understanding of Python functions, including function syntax, parameters, arguments, nested functions, lambda expressions, recursion, variable scope, type hints, and keyword arguments.

- **Chapter:** 1 — Functions
- **Assessment:** Function Summative Test Quiz
- **Total Questions:** 20
- **Programming Language:** Python
- **Format:** Multiple-choice questions with answers

---

## Questions and Answers

### Question 1: Defining a Function

**Question:** Which line correctly defines a function named `greet` that takes no parameters?

- a. `def greet() {`
- b. `def greet():`
- c. `def greet:`

**Answer:** b. `def greet():`

### Question 2: Nested Functions

**Question:** What is a nested function?

- a. A function defined inside another function
- b. A function with default parameters
- c. A function that takes another function as an argument
- d. A function that calls itself

**Answer:** a. A function defined inside another function.

### Question 3: Passing Functions as Arguments

**Question:** What does this code print?

```python
def apply(fn, value):
    return fn(value)

print(apply(abs, -7))
```

- a. `-7`
- b. `7`
- c. `abs`
- d. `TypeError`

**Answer:** b. `7`

**Explanation:** The built-in `abs()` function returns the absolute value of `-7`, which is `7`.

### Question 4: Docstrings

**Question:** What is a docstring?

- a. A variable that stores documentation
- b. A special type of parameter
- c. A string literal placed as the first line of the function body
- d. A comment starting with a special symbol

**Answer:** c. A string literal placed as the first statement in the function body.

### Question 5: Lambda Functions

**Question:** Which statement about lambda functions is true?

- a. They are anonymous functions written in one expression
- b. They cannot take arguments
- c. They must be given a name with `def`
- d. They always return `None`

**Answer:** a. They are anonymous functions written in one expression.

### Question 6: Valid Function Names

**Question:** Which of these is a valid function name?

- a. `my-func`
- b. `def`
- c. `calculate_total`
- d. `2nd_try`

**Answer:** c. `calculate_total`

### Question 7: Naming Conventions

**Question:** By convention, Python function names are written in:

- a. UPPERCASE
- b. `snake_case`
- c. `PascalCase`
- d. `camelCase`

**Answer:** b. `snake_case`

### Question 8: Returning Values

**Question:** What does this code print?

```python
def double(x):
    return x * 2

print(double(3))
```

- a. `x * 2`
- b. `6`
- c. `3`
- d. `None`

**Answer:** b. `6`

**Explanation:** The function multiplies `3` by `2` and returns `6`.

### Question 9: Code After Return

**Question:** What happens to code written after a `return` statement inside a function?

- a. It always runs
- b. It runs only inside loops
- c. It never runs once the `return` executes
- d. It causes a syntax error

**Answer:** c. It never runs once the `return` executes.

### Question 10: Function Keyword

**Question:** Which keyword is used to define a function in Python?

- a. `def`
- b. `define`
- c. `function`
- d. `fun`

**Answer:** a. `def`

### Question 11: Variable Scope

**Question:** What does this code print?

```python
x = 10

def change():
    x = 5

change()
print(x)
```

- a. `10`
- b. `None`
- c. `5`
- d. `NameError`

**Answer:** a. `10`

**Explanation:** The variable `x = 5` is local to the function. It does not modify the global variable `x`, which remains `10`.

### Question 12: Recursion

**Question:** What must every recursive function include to avoid infinite recursion?

- a. A `while` loop
- b. A global variable
- c. A base case that stops the recursion
- d. At least two parameters

**Answer:** c. A base case that stops the recursion.

### Question 13: Return vs Print

**Question:** What is the difference between `return` and `print`?

- a. They are identical
- b. Only `print` can be used inside functions
- c. `print` sends a value back to the caller; `return` displays it
- d. `return` sends a value back to the caller; `print` displays it on screen

**Answer:** d. `return` sends a value back to the caller; `print` displays it on screen.

### Question 14: Keyword Arguments

**Question:** What does `**kwargs` collect inside a function?

- a. Extra keyword arguments, as a dictionary
- b. Extra positional arguments, as a list
- c. Default values only
- d. The docstring

**Answer:** a. Extra keyword arguments, as a dictionary.

### Question 15: Factorial and Recursion

**Question:** What does this code print?

```python
def fact(n):
    if n < 1:
        return 1
    return n * fact(n - 1)

print(fact(4))
```

- a. `1`
- b. `4`
- c. `24`
- d. `10`

**Answer:** c. `24`

**Explanation:** The function calculates the factorial of 4:

\[
4! = 4 \times 3 \times 2 \times 1 = 24
\]

### Question 16: Type Hints

**Question:** Are Python type hints enforced at runtime?

- a. No, they are hints for readers and tools
- b. Yes, wrong types raise `TypeError`
- c. Only inside classes
- d. Only for parameters

**Answer:** a. No, they are hints for readers and tools.

### Question 17: Return Type Hints

**Question:** In `def f(x: int) -> str:`, what does `-> str` indicate?

- a. A hint that the function returns a string
- b. That the function must return
- c. The type of parameter `x`
- d. A default value

**Answer:** a. A hint that the function returns a string.

### Question 18: Local Scope

**Question:** A variable created inside a function body has what kind of scope?

- a. Universal
- b. Built-in
- c. Local
- d. Global

**Answer:** c. Local.

### Question 19: Keyword Argument Order

**Question:** What does this code print?

```python
def sub(a, b):
    return a - b

print(sub(b=2, a=10))
```

- a. `TypeError`
- b. `12`
- c. `8`
- d. `-8`

**Answer:** c. `8`

**Explanation:** Keyword arguments assign `10` to `a` and `2` to `b`. The calculation is `10 - 2 = 8`.

### Question 20: Keyword Argument Calls

**Question:** Which call below uses a keyword argument?

- a. `f[5]`
- b. `f(x=5)`
- c. `5, makes it a keyword argument.`
- d. `f(5)`
- e. `f(*5)`

**Answer:** b. `f(x=5)`

**Explanation:** The expression `x=5` explicitly identifies the parameter by name.

---

## Summary of Correct Answers

| Question | Answer |
|---:|---|
| 1 | b |
| 2 | a |
| 3 | b |
| 4 | c |
| 5 | a |
| 6 | c |
| 7 | b |
| 8 | b |
| 9 | c |
| 10 | a |
| 11 | a |
| 12 | c |
| 13 | d |
| 14 | a |
| 15 | c |
| 16 | a |
| 17 | a |
| 18 | c |
| 19 | c |
| 20 | b |

---

## Key Learning Outcomes

After completing this assessment, learners should be able to:

- Define and call Python functions.
- Identify valid function names and follow naming conventions.
- Understand nested functions, lambda expressions, and docstrings.
- Distinguish between parameters, arguments, `print()`, and `return`.
- Explain local variable scope and keyword arguments.
- Understand recursion, base cases, and factorial calculations.
- Interpret Python type hints and return type annotations.

## Conclusion

The Function Summative Test Quiz reinforces the essential concepts of Python functions and provides a foundation for writing modular, reusable, and maintainable Python programs.

**Recommended filename:** `README.md`
