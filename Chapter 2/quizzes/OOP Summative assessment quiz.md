# Python Note-Taking App — Quiz Questions and Answers

## 📘 Overview

This quiz covers essential Python programming concepts used to build a persistent note-taking application. Topics include Object-Oriented Programming (OOP), classes, inheritance, JSON, file operations, exception handling, and managing collections of objects.

## 🎯 Learning Objectives

- Understand classes, objects, and methods.
- Use constructors and the `self` keyword.
- Apply inheritance and `super()`.
- Work with JSON data and files.
- Handle exceptions using `try`, `except`, and `finally`.
- Store application data persistently.
- Design a note-taking application using `Note` and `Notebook` classes.

---

## 📝 Quiz Questions and Answers

### Question 1: What does raising an exception manually with `raise ValueError('message')` do?

**Answer: A — Deliberately triggers an exception with a custom message, which can be caught by an `except` block elsewhere.**

The `raise` statement allows a program to signal that an error or invalid condition has occurred.

```python
raise ValueError("Invalid input")
```

### Question 2: Why is JSON a good format for saving structured app data?

**Answer: A — It maps naturally onto Python lists and dictionaries, making it easy to save and load structured data.**

JSON supports structured data and can be exchanged between different programming languages.

### Question 3: What is the parent class commonly called in an inheritance relationship?

**Answer: C — The superclass (or base class).**

A superclass provides attributes and methods that subclasses can inherit.

### Question 4: What is the benefit of modelling a real-world entity, like a bank account, as a class rather than several separate variables?

**Answer: A — Classes bundle related data and behaviour together, making the code easier to organise, reuse, and extend.**

Classes keep related attributes and methods together in a structured unit.

### Question 5: If `t1 = Task('Buy milk')` and `t2 = Task('Walk dog')`, what happens to `t2.name` when `t1.name` changes to `'Buy bread'`?

**Answer: C — It remains `'Walk dog'`, unaffected.**

Each object normally has its own instance attributes.

### Question 6: What happens if you try to open a file with mode `'r'` and the file does not exist?

**Answer: B — A `FileNotFoundError` is raised.**

Python raises this exception when a requested file cannot be found for reading.

### Question 7: What is the correct pattern for saving a list of dictionaries called `notes` to `notes.json`?

**Answer: B — `with open('notes.json', 'w') as f: json.dump(notes, f)`**

```python
import json

with open("notes.json", "w") as f:
    json.dump(notes, f)
```

This writes the list to a JSON file. The variable `notes` must already contain the data to save.

### Question 8: What is the purpose of a `try` block?

**Answer: D — To attempt an operation that might fail, without letting an unhandled error crash the whole program.**

A `try` block allows exceptions to be handled using `except` blocks.

### Question 9: Given `class Admin(User): def __init__(self, name, level): super().__init__(name); self.level = level`, what does this constructor do?

**Answer: C — It calls `User`'s `__init__()` to set up shared attributes, then adds an `Admin`-specific `level` attribute.**

The `super()` function allows the subclass to reuse the parent's initialisation logic.

### Question 10: What is the correct way to give a `Note` object a title attribute inside `__init__()`?

**Answer: F — `self.title`**

Example:

```python
class Note:
    def __init__(self, title):
        self.title = title
```

### Question 11: Which combination best describes a robust, persistent note-taking app's architecture?

**Answer: A — A `Note` class for individual data, a `Notebook` manager class, JSON file storage, and `try/except` around file operations.**

This design separates individual notes, collection management, persistent storage, and error handling.

### Question 12: What does `self.notes.append(new_note)` do inside a `Notebook` method?

**Answer: B — Adds `new_note` to the end of this `Notebook` instance's notes list.**

The `append()` method adds an item to the end of a list.

```python
self.notes.append(new_note)
```

### Question 13: A subclass `Admin` inherits from `User` but does not define its own `__init__()` method. What happens when `Admin('Thabo')` is created?

**Answer: B — Python automatically uses `User`'s `__init__()` method since `Admin` did not override it.**

The inherited initialisation method is used if it is available and compatible with the arguments supplied.

### Question 14: What is the safest way to open a file for reading in Python?

**Answer: A — `with open('notes.txt', 'r') as f:`**

The `with` statement automatically closes the file when the block finishes, including when an exception occurs.

### Question 15: Why should file operations in a persistent app almost always be wrapped in `try/except`?

**Answer: A — Because a missing or corrupted file could otherwise cause an unhandled error and interrupt the program.**

Exception handling allows the application to respond to file errors appropriately.

### Question 16: What is the purpose of a `finally` block?

**Answer: A — It runs whether the `try` block succeeds or an exception is caught.**

A `finally` block is commonly used for cleanup tasks. It normally executes regardless of whether an exception occurred.

### Question 17: How do you call a method named `mark_done` on an object called `t`?

**Answer: A — `t.mark_done()`**

The dot operator accesses the method through the object.

### Question 18: What does `super().__init__(...)` do inside a subclass's `__init__()` method?

**Answer: B — Calls the parent class's initialisation method so shared setup logic is not duplicated.**

Example:

```python
class User:
    def __init__(self, name):
        self.name = name

class Admin(User):
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level
```

### Question 19: What is the purpose of the `__init__()` method in a class?

**Answer: B — It runs automatically during normal object initialisation to set up initial attributes.**

Example:

```python
class Task:
    def __init__(self, name):
        self.name = name
```

### Question 20: In a Notebook app, what is the role of a manager class such as `Notebook`?

**Answer: A — It manages a whole collection of `Note` objects, including loading, saving, adding, and deleting them.**

The manager class coordinates operations involving the collection rather than representing just one note.

---

## 🔑 Key Concepts Summary

| Concept | Purpose |
|---|---|
| Class | Defines attributes and behaviour for objects |
| Object | An instance of a class |
| `__init__()` | Initialises a newly created object |
| `self` | Refers to the current instance |
| Inheritance | Allows a class to reuse functionality from a parent class |
| `super()` | Accesses functionality through the inheritance chain |
| JSON | Stores and exchanges structured data |
| `json.dump()` | Writes JSON data to a file object |
| `try` | Contains code that may raise an exception |
| `except` | Handles specified exceptions |
| `finally` | Performs cleanup whether an exception occurs or not |
| `append()` | Adds an item to a list |
| `open()` | Opens a file |
| Persistent storage | Preserves information after a program ends |

## 📚 Conclusion

A reliable note-taking application combines OOP principles with JSON file storage and exception handling. Using separate classes for individual notes and notebook management makes the application easier to organise, maintain, and extend.

---

**Topic:** Python Note-Taking App  
**Assessment:** 20 Questions and Answers  
**Focus Areas:** OOP, Inheritance, JSON, File Handling, Exception Handling and Persistent Storage
