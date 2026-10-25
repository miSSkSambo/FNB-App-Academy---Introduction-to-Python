# Flet App Development – 20 Questions and Answers

## Introduction

This quiz covers the fundamentals of Flet app development using Python, including UI controls, events, layouts, virtual environments, and running Flet applications.

## Questions and Answers

### Question 1
**Changing a control's property in code is enough on its own to make the change appear on screen, with no further call needed.**

**Answer:** False

**Explanation:** In the usual Flet update workflow, call `page.update()` to send changes to the UI.

### Question 2
**Which event fires every time the text inside a TextField changes, useful for live validation as the user types?**

- a. `on_input`
- b. `on_change`
- c. `on_key`
- d. `on_submit`

**Answer:** b. `on_change`

**Explanation:** The `on_change` event is used to respond when a TextField's value changes.

### Question 3
**What is the Container control mainly used for?**

- a. Wrapping a control to apply background colour, padding, borders, sizing, and alignment
- b. Storing data between sessions
- c. Making a Row scroll horizontally
- d. Displaying plain text only

**Answer:** a. Wrapping a control to apply background colour, padding, borders, sizing, and alignment

### Question 4
**A Flet script's main function typically receives which object as a parameter, used to build and display the UI?**

- a. `window`
- b. `app`
- c. `screen`
- d. `page`

**Answer:** d. `page`

**Explanation:** The `page` object represents the app's page and is used to add and manage UI controls.

### Question 5
**Flet apps require writing separate HTML and CSS files to control their appearance.**

**Answer:** False

**Explanation:** Flet allows developers to build user interfaces using Python.

### Question 6
**Setting a button's disabled property to True right before a slow network call, then back to False afterward, mainly helps prevent what?**

- a. The app from crashing
- b. The user clicking the button again and double-submitting the action
- c. The button from ever being visible again
- d. The network call from timing out

**Answer:** b. The user clicking the button again and double-submitting the action

### Question 7
**A Container can hold only one direct child, but that child can itself be a Row, Column, or another Container holding multiple controls.**

**Answer:** True

### Question 8
**Which command creates a Python virtual environment named `venv`?**

- a. `venv --new`
- b. `python -m venv venv`
- c. `python create venv`
- d. `pip install venv`

**Answer:** b. `python -m venv venv`

### Question 9
**Which line correctly starts a Flet app, using the current entry point syntax?**

- a. `main.run()`
- b. `flet.launch(main)`
- c. `ft.app(target=main)`
- d. `ft.run(main)`

**Answer:** d. `ft.run(main)`

### Question 10
**Which property on a GestureDetector runs a function when its content is tapped?**

- a. `on_press`
- b. `on_tap`
- c. `on_click`
- d. `on_select`

**Answer:** b. `on_tap`

### Question 11
**Which property on a Row or Column sets a fixed gap between its children, without needing separate spacer controls?**

- a. `gap`
- b. `padding`
- c. `margin`
- d. `spacing`

**Answer:** a. `gap`

### Question 12
**What is required at minimum before Flet can be installed and used at all?**

- a. A separately installed Flutter SDK
- b. A working Python installation and pip
- c. Node.js
- d. Docker

**Answer:** b. A working Python installation and pip

### Question 13
**Checkbox and Slider controls both support an on_change event that fires as the user interacts with them.**

**Answer:** True

### Question 14
**Which property on a Container controls the thickness and colour of its outline, separate from its fill colour?**

- a. `outline_color`
- b. `stroke`
- c. `bgcolor`
- d. `border`

**Answer:** d. `border`

### Question 15
**By default, flet run only watches the exact script you ran for changes, not other files in the same folder.**

**Answer:** True

### Question 16
**What is the purpose of the assets folder created by flet create?**

- a. It stores static files the app can reference, such as images, icons, and fonts
- b. It stores compiled executable files only
- c. It stores unit test files
- d. It stores the Python virtual environment

**Answer:** a. It stores static files the app can reference, such as images, icons, and fonts

### Question 17
**A control's visible property is set to False and update is called. What happens to that control?**

- a. Its colour changes to match the background
- b. It is permanently deleted from the app
- c. It is hidden on screen but still exists and can be shown again later
- d. It moves to a different part of the layout

**Answer:** c. It is hidden on screen but still exists and can be shown again later

### Question 18
**The Stack control lays its children out one after another in a list, never allowing them to overlap.**

**Answer:** False

**Explanation:** A `Stack` allows controls to be layered and overlap.

### Question 19
**A Row will automatically wrap its children onto a new line if they don't fit the available width, with no extra configuration.**

**Answer:** False

**Explanation:** A standard `Row` does not automatically wrap its children onto another line.

### Question 20
**Assigning a control to a variable, instead of writing it inline inside a layout, is necessary if you need to read or update that control's properties later from a function.**

**Answer:** True

**Explanation:** Assigning a control to a variable makes it straightforward to reference and update that control later.

---

## Summary

This quiz tests understanding of:

- Flet UI controls and layouts
- Event handling and user interaction
- Updating controls with `page.update()`
- Python virtual environments
- Running Flet applications
- Containers, Rows, Columns, and Stacks
- Managing control properties and visibility

## Technologies Covered

- Python
- Flet
- Visual Studio Code
- Python virtual environments

**End of Quiz – 20 Questions and Answers**
