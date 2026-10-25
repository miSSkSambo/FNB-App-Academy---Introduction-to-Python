# Python Flet — Quiz Questions and Answers

## 📘 Overview

This quiz covers the basics of Flet, a Python framework for building cross-platform applications. It includes UI rendering, virtual environments, package installation, running applications, and cross-platform development.

## 🎯 Learning Objectives

- Understand what Flet uses to render its user interface.
- Create and activate Python virtual environments on Windows.
- Install Flet using pip.
- Run Flet applications during development.
- Understand how Flet supports desktop, web, and mobile applications.

---

## 📝 Quiz Questions and Answers

### Question 1: What does Flet use under the hood to render its UI?

**Answer: A — Google's Flutter.**

Flet uses Flutter technology to render user interfaces while allowing developers to write application logic in Python.

### Question 2: Which command creates a Python virtual environment on Windows?

**Answer: C — `python -m venv venv`**

This command creates a virtual environment named `venv` in the current project directory.

```bash
python -m venv venv
```

### Question 3: After creating a virtual environment on Windows PowerShell, which command activates it?

**Answer: A — `venv\Scripts\activate`**

In PowerShell, the commonly used activation command is:

```powershell
.\venv\Scripts\Activate.ps1
```

This activates the virtual environment so packages can be installed separately for the project.

### Question 4: Which command installs Flet using pip?

**Answer: A — `pip install flet`**

Run this command in the terminal after activating your virtual environment.

```bash
pip install flet
```

### Question 5: Which terminal command runs a Flet app with live or hot reload during development?

**Answer: D — `flet run`**

For example, to run an application saved in `main.py`, use:

```bash
flet run main.py
```

Flet supports hot reload during development, allowing changes to be reflected without manually restarting the app in supported workflows.

### Question 6: You need to write separate HTML/CSS files to style a Flet app, similar to a website.

**Answer: False.**

Flet allows developers to create and style UI components directly in Python without requiring separate HTML and CSS files for the normal UI workflow.

### Question 7: You should install Flet globally instead of inside a virtual environment, so it is available to every project.

**Answer: False.**

Installing Flet inside a virtual environment keeps dependencies isolated for each project and helps prevent package conflicts.

### Question 8: A Flet app can be built once in Python and potentially run as a desktop, web, or mobile app without rewriting the UI code for each platform.

**Answer: True.**

Flet supports building applications for multiple platforms using Python. Some platform-specific configuration or adjustments may still be required.

---

## 💻 Quick Setup Guide

Follow these steps to create and run a basic Flet project on Windows.

### Step 1: Create a project folder

```bash
mkdir my_flet_app
cd my_flet_app
```

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

### Step 3: Activate the environment

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install Flet

```bash
pip install flet
```

### Step 5: Create `main.py`

```python
import flet as ft


def main(page: ft.Page):
    page.title = "My First Flet App"
    page.add(
        ft.Text("Hello, Flet!"),
        ft.Button("Click Me")
    )


ft.run(main)
```

### Step 6: Run the application

```bash
flet run main.py
```

**Note:** Flet APIs may vary between versions. If a control constructor differs in your installed version, consult the documentation for that version.

---

## 🔑 Key Concepts Summary

| Concept | Description |
|---|---|
| Flet | A Python framework for building cross-platform applications |
| Flutter | The UI technology Flet uses under the hood |
| Virtual environment | An isolated Python environment for a project |
| `venv` | Python's built-in module for creating virtual environments |
| `pip` | A tool for installing Python packages |
| `flet run` | Runs a Flet application during development |
| Hot reload | Reflects supported code changes during development |
| Cross-platform development | Building for desktop, web, and mobile from a shared codebase |

## 📚 Conclusion

Flet makes it possible to develop interactive applications using Python while supporting multiple platforms. Understanding virtual environments, package installation, and development commands provides a strong foundation for building and running Flet projects.

---

**Topic:** Python Flet Framework  
**Assessment:** 8 Questions and Answers  
**Purpose:** Revision and assessment preparation
