# Python OOP Quiz — Inheritance, Composition and Polymorphism

## 📘 Overview

This quiz covers key Object-Oriented Programming (OOP) concepts in Python, including inheritance, composition, polymorphism, and the `super()` keyword.

## 🎯 Learning Objectives

- Understand inheritance and parent-child class relationships.
- Explain composition and the “has-a” relationship.
- Differentiate between inheritance and composition.
- Understand polymorphism and method overriding.
- Use `super()` to access parent-class functionality.
- Recognise inheritance in Python code.
- Understand the benefits of code reuse.

---

## 📝 Quiz Questions and Answers

### Question 1: A `Vehicle` class has a `run()` method. `Car` and `Helicopter` inherit from `Vehicle` and define their own `run()` methods. Which OOP concepts are demonstrated?

**Answer: D — Inheritance and Polymorphism.**

Inheritance allows `Car` and `Helicopter` to derive from `Vehicle`. Polymorphism allows each class to implement `run()` differently.

### Question 2: Why is composition a good way to model animals in a `Zoo` application?

**Answer: B — The zoo can hold different animals, and new animal classes can be added without changing the `Zoo` class itself.**

Composition allows a class to contain objects of other classes, making the application more flexible and easier to maintain.

### Question 3: True or False: A parent class can only have one child class.

**Answer: B — False.**

A parent class can have multiple child classes.

Example:

```python
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass
```

Both `Dog` and `Cat` inherit from `Animal`.

### Question 4: True or False: If one child class defines a method that is not in its parent class, that method can automatically be called by any other child class.

**Answer: B — False.**

A method defined only in one child class is not automatically available to sibling classes.

### Question 5: What does polymorphism mean in OOP?

**Answer: D — Different classes in an inheritance relationship can use the same method name with different functionality.**

Example:

```python
class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"
```

Both classes have a `speak()` method, but each behaves differently.

### Question 6: What is composition in Object-Oriented Programming?

**Answer: B — A design principle where one class has instances of another class and uses their attributes and methods to perform tasks.**

Composition builds complex objects by combining objects from other classes.

Example:

```python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()
```

A `Car` contains an `Engine` object.

### Question 7: What is the key difference between composition and inheritance?

**Answer: A — Composition models a “has-a” relationship, while inheritance models an “is-a” relationship.**

- **Composition:** A car has an engine.
- **Inheritance:** A dog is an animal.

### Question 8: What is the purpose of the `super()` keyword?

**Answer: D — It is used to call methods from a parent class in the inheritance chain.**

Example:

```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return super().speak() + " - Woof"
```

`super()` provides access to the parent implementation according to Python's method resolution order.

### Question 9: Which code snippet demonstrates inheritance?

**Answer: B —**

```python
class Animal:
    def speak(self):
        print("make sound")

class Dog(Animal):
    pass
```

The expression `class Dog(Animal):` shows that `Dog` inherits from `Animal`.

### Question 10: Why would we use inheritance in OOP?

**Answer: C — It allows code reuse between related classes, reducing duplication and speeding up development.**

Inheritance enables child classes to reuse or customise functionality defined in parent classes.

---

## 🔑 Key Concepts Summary

| Concept | Meaning | Example |
|---|---|---|
| Inheritance | A child class derives from a parent class | `Dog(Animal)` |
| Composition | One object contains another object | A car has an engine |
| Polymorphism | The same method name can behave differently | `Dog.speak()` and `Cat.speak()` |
| `super()` | Accesses functionality through the parent-class method resolution order | `super().speak()` |
| Method overriding | A child class provides its own implementation of an inherited method | Redefining `speak()` |
| Code reuse | Reusing existing functionality rather than duplicating it | Shared methods in `Animal` |

## 📚 Conclusion

Inheritance, composition, and polymorphism are important OOP concepts that help developers create flexible, reusable, and maintainable Python applications. Understanding when to use each concept supports better software design.

---

**Topic:** Python Object-Oriented Programming  
**Assessment:** 10 Questions and Answers  
**Focus Areas:** Inheritance, Composition, Polymorphism and `super()`
