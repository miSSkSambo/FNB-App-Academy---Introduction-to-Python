# Python Quiz — File Handling, JSON and Exception Handling

## 📘 Overview

This quiz covers important Python concepts, including exception handling, file operations, JSON data processing, and persistent storage.

## 🎯 Learning Objectives

- Understand `try` and `except` blocks.
- Recognise the importance of specific exceptions.
- Understand persistent data storage.
- Differentiate between JSON `dump()`, `dumps()`, `load()`, and `loads()`.
- Learn Python file-opening modes.
- Identify built-in functions and modules for file handling.

---

## 📝 Quiz Questions and Answers

### Question 1: Why is it a good idea to explicitly define the exception you expect to occur?

**Answer: D — It makes the intended failure case clear and allows assumptions to be made regarding the state of the program at that point in time.**

Catching specific exceptions makes code clearer and helps prevent unrelated errors from being hidden.

Example:

```python
try:
    number = int("abc")
except ValueError:
    print("Please enter a valid number.")
```

### Question 2: Why do we consider long-term storage for applications?

**Answer: C — Information stored and produced in programs may be lost once the program completes unless it is saved to persistent storage.**

Files and databases allow information to remain available after a program closes.

### Question 3: What is the difference between `dump()` and `dumps()` in Python's JSON module?

**Answer: C — `dump()` writes JSON to a file object, while `dumps()` returns JSON as a string.**

Example:

```python
import json

data = {"name": "Alex", "age": 25}

# Write JSON to a file
with open("data.json", "w") as file:
    json.dump(data, file)

# Convert Python data into a JSON string
json_string = json.dumps(data)
print(json_string)
```

### Question 4: What does every `try` block need in order to handle errors properly?

**Answer: B — None of the above.**

A `try` block must be followed by at least one `except` block, a `finally` block, or both. An `except` block does not always need to specify an exception type, although specific exceptions are generally recommended.

### Question 5: What is the difference between `load()` and `loads()` in Python's JSON module?

**Answer: A — `load()` reads JSON from file objects, while `loads()` reads JSON from a string.**

Example:

```python
import json

# Read JSON from a file
with open("data.json", "r") as file:
    data = json.load(file)

# Read JSON from a string
json_text = '{"name": "Alex", "age": 25}'
data_from_string = json.loads(json_text)
```

### Question 6: True or False — A `try` block can only be followed by one `except` block.

**Answer: A — False.**

A `try` block can have multiple `except` blocks to handle different exceptions.

Example:

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Enter a valid integer.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
```

### Question 7: What does the file mode `'w'` do when opening a file?

**Answer: A — Opens the file to write content, overwriting the file if it already exists.**

If the file does not exist, Python creates it. If it exists, its previous contents are truncated.

Example:

```python
with open("notes.txt", "w") as file:
    file.write("Hello, Python!")
```

### Question 8: Which built-in Python module is used to work with JSON data and JSON files?

**Answer: A — `json`.**

The `json` module provides functions to convert between Python objects and JSON data.

Example:

```python
import json
```

### Question 9: Which of the following is not a valid standard file-opening mode?

**Answer: B — `'q'`.**

Common file modes include:

- `'r'` — Read a file.
- `'w'` — Write and overwrite a file.
- `'a'` — Append content to a file.
- `'x'` — Create a new file, failing if it already exists.

The mode `'q'` is not a standard Python file-opening mode.

### Question 10: Which built-in function is used to open a file in Python?

**Answer: D — `open()`.**

The `open()` function opens a file and returns a file object.

Example:

```python
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
```

Using `with` automatically closes the file when the block finishes.

---

## 🔑 Key Concepts Summary

| Concept | Purpose |
|---|---|
| `try` | Executes code that may raise an exception |
| `except` | Handles an exception |
| `finally` | Runs cleanup code whether an exception occurs or not |
| Persistent storage | Keeps data available after a program ends |
| `json.dump()` | Writes JSON data to a file object |
| `json.dumps()` | Converts Python data into a JSON string |
| `json.load()` | Reads JSON data from a file object |
| `json.loads()` | Parses JSON data from a string |
| `'r'` | Opens a file for reading |
| `'w'` | Opens a file for writing and truncates existing contents |
| `'a'` | Opens a file for appending |
| `open()` | Opens a file |

## 📚 Conclusion

Exception handling helps Python programs respond to errors, while file handling and JSON allow applications to save, retrieve, and exchange information. Understanding these concepts is essential for developing reliable applications that manage data effectively.

---

**Topic:** Python File Handling, JSON and Exception Handling  
**Assessment:** 10 Questions and Answers  
**Purpose:** Revision and assessment preparation
