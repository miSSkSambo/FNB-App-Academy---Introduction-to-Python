# Python Flet — Layout Controls and Login Page Quiz

## 📘 Overview

This quiz covers the fundamentals of designing user interfaces with Flet in Python. It focuses on layout controls, containers, colours, padding, alignment, stacking, and login form functionality.

## 🎯 Learning Objectives

- Understand the purpose of `ft.Row`, `ft.Column`, `ft.Container`, and `ft.Stack`.
- Arrange UI controls horizontally and vertically.
- Apply colours, padding, borders, sizing, and alignment.
- Understand the difference between padding and margin.
- Learn how login fields can connect to validation functions.

---

## 📝 Quiz Questions and Answers

### Question 1: Which layout control stacks its child controls vertically, one below another?

**Answer: B — `ft.Column`**

A Column arranges controls vertically, placing each control below the previous one.

```python
ft.Column(
    controls=[
        ft.Text("Username"),
        ft.Text("Password"),
    ]
)
```

### Question 2: Which layout control arranges its children side by side, horizontally?

**Answer: B — `ft.Row`**

A Row arranges controls horizontally, placing them next to each other.

```python
ft.Row(
    controls=[
        ft.Icon(ft.Icons.PERSON),
        ft.Text("Username"),
    ]
)
```

### Question 3: What is `ft.Container` mainly used for?

**Answer: D — Wrapping a control or controls to apply background colour, padding, borders, sizing, and alignment.**

A Container helps style and position content within a UI.

```python
ft.Container(
    content=ft.Text("Welcome"),
    padding=20,
    bgcolor=ft.Colors.BLUE,
    border_radius=10,
)
```

### Question 4: In the login page, which control was used to arrange the person icon and Username label next to each other?

**Answer: C — `ft.Row`**

A Row places the icon and label horizontally beside each other.

### Question 5: Which property on `ft.Column` or `ft.Row` controls how children are positioned along the main axis?

**Answer: C — `alignment` (as given in the quiz options).**

The relevant property in current Flet APIs is generally `alignment`, used to control positioning along the main axis. In some versions or examples, `main_axis_alignment` may be used.

### Question 6: Which two ways of specifying a colour were demonstrated on the login page? (Select 2)

**Answers: A and D — A named colour constant from `ft.Colors` and a hex code string.**

Examples:

```python
# Named colour
bgcolor = ft.Colors.RED

# Hexadecimal colour
bgcolor = "#0084A8"
```

Both approaches can be used to specify colours in Flet.

### Question 7: Setting a Container's padding adds empty space outside the container, between it and other controls.

**Answer: False.**

Padding adds space inside the container, between its content and its edges. Margin is used to create space outside the container.

### Question 8: `ft.Stack` arranges controls one after another in a list, with no overlap allowed.

**Answer: False.**

A Stack allows controls to be layered and overlap, which is useful for overlays and positioned elements.

### Question 9: A Container can hold only one direct child, but that child can itself be a Row, Column, or another Container holding multiple controls.

**Answer: True.**

A Container has one direct `content` control. That control can be a layout such as a Row or Column containing multiple controls.

### Question 10: In the lesson's login page, were the username and password fields connected to functions that checked whether the values were correct?

**Answer: True.**

Based on the lesson description, the fields were connected to functions that checked whether the entered values were correct.

---

## 🔑 Key Concepts Summary

| Control or Property | Purpose |
|---|---|
| `ft.Row` | Arranges controls horizontally |
| `ft.Column` | Arranges controls vertically |
| `ft.Container` | Wraps and styles content |
| `ft.Stack` | Layers controls, allowing overlap |
| `content` | Specifies a Container's direct child |
| `padding` | Adds space inside a container |
| `margin` | Adds space outside a control |
| `alignment` | Controls positioning along the main axis in applicable Flet APIs |
| `ft.Colors.RED` | Specifies a named colour |
| Hex colour | Specifies a colour using a value such as `"#0084A8"` |

## 📚 Conclusion

Flet provides Python controls for creating interactive and visually organised user interfaces. Understanding layout controls, styling, colour formats, and input validation helps developers build login pages and other application screens effectively.

---

**Topic:** Python Flet UI Design  
**Assessment:** 10 Questions and Answers  
**Focus Areas:** Layout Controls, Containers, Colours, Alignment and Login Forms
