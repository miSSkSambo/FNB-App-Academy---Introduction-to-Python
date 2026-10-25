# Object-Oriented Programming (OOP) — Quiz Questions and Answers

## 📘 Overview

This quiz covers the fundamentals of Object-Oriented Programming (OOP) in Python. It introduces classes, objects, constructors, instance methods, the `self` keyword, abstraction, and the main advantages of using OOP.

## 🎯 Learning Objectives

- Understand the purpose of classes and objects.
- Learn how to instantiate objects in Python.
- Understand constructors and the `__init__()` method.
- Explain the role of the `self` keyword.
- Identify real-world examples of abstraction.
- Understand the benefits of OOP.

---

## 📝 Quiz Questions and Answers

### Question 1: Can a class's methods have parameters other than the mandatory `self` parameter?

**Answer: B — False.**

Python methods can accept additional parameters besides `self`.

Example:

```python
class Car:
    def drive(self, speed):
        return f"Driving at {speed} km/h"
```

Here, `speed` is an additional parameter.

### Question 2: What does a class require in order to be instantiated into an object?

**Answer: D — A constructor.**

A constructor, commonly associated with the `__init__()` method in Python, initialises an object when it is created. However, Python classes can still be instantiated without explicitly defining `__init__()`.

### Question 3: What is a class in Object-Oriented Programming?

**Answer: B — A blueprint that defines the data and functionality that an instantiated object can have.**

A class defines the attributes and methods that its objects can use.

Example:

```python
class Car:
    def __init__(self, colour):
        self.colour = colour
```

### Question 4: What is Object-Oriented Programming?

**Answer: C — A programming style based around grouping data and related functions into self-contained units.**

OOP organises related data and behaviour into objects created from classes.

### Question 5: What is the correct way to create an object for a class named `Car`?

**Answer: E — `Car()`**

A class is called to create an instance. You can assign the object to a variable:

```python
myCar = Car()
```

### Question 6: What is the purpose of `__init__()` in a Python class?

**Answer: B — It initialises an object when an object is created from the class.**

The `__init__()` method is automatically called during normal object initialisation and is commonly used to set initial attribute values.

Example:

```python
class Car:
    def __init__(self, wheels):
        self.wheels = wheels
```

### Question 7: What purpose does the `self` keyword serve?

**Answer: C — It refers to methods and attributes for the currently instantiated object.**

The `self` parameter allows instance methods to access or modify the attributes of the particular object.

Example:

```python
class Car:
    def __init__(self, colour):
        self.colour = colour
```

Here, `self.colour` belongs to the individual object.

### Question 8: Which is a real-world example of abstraction in OOP?

**Answer: C — A light switch to turn a bulb on and off.**

A light switch provides a simple way to control a light without requiring the user to understand the electrical system behind it.

### Question 9: Which is the correct Python constructor for a class `Car` that accepts the number of wheels as an argument?

**Answer: A — `__init__(self, numWheels)`**

The correct method definition includes double underscores before and after `init`:

```python
class Car:
    def __init__(self, numWheels):
        self.numWheels = numWheels
```

An object can then be created with a specified number of wheels:

```python
myCar = Car(4)
```

### Question 10: Which list gives the main reasons for writing Object-Oriented Code?

**Answer: A — Reusability, Maintainability, Organisation and Abstraction.**

These benefits help developers structure code, reduce duplication, simplify maintenance, and hide unnecessary implementation details.

---

## 🔑 Key Concepts Summary

| Concept | Description |
|---|---|
| Class | A blueprint for creating objects |
| Object | An instance of a class |
| Constructor | Initialises a newly created object |
| `__init__()` | Python method commonly used to initialise attributes |
| `self` | Refers to the current instance |
| Abstraction | Hides implementation complexity behind a simpler interface |
| Reusability | Allows code and behaviour to be reused |
| Maintainability | Makes code easier to update and fix |

## 💻 Practical Example

```python
class Car:
    def __init__(self, colour, wheels):
        self.colour = colour
        self.wheels = wheels

    def describe(self):
        return f"My car is {self.colour} and has {self.wheels} wheels."


myCar = Car("blue", 4)

print(myCar.describe())
```

**Output:**

```text
My car is blue and has 4 wheels.
```

## 📚 Conclusion

Object-Oriented Programming helps developers organise programs using classes and objects. Understanding constructors, instance attributes, methods, and abstraction provides a strong foundation for writing reusable and maintainable Python applications.

---

**Topic:** Object-Oriented Programming in Python  
**Assessment:** 10 Questions and Answers  
**Purpose:** Revision and assessment preparation
