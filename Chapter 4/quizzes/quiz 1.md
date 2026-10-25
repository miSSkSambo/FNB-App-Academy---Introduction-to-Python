# Flet Dialogs, Password Reset and JSON File Handling Quiz

## Overview

This quiz covers dialog management, multi-step user interactions, password reset flows, input validation, session storage, and JSON file handling in Python using the Flet framework.

## Questions and Answers

### Question 1: Setting `modal=True` on a dialog means the user can tap outside it to dismiss it without making a choice.

**Answer: False**

**Explanation:** A modal dialog blocks interaction with the underlying screen while it is open. Setting `modal=True` does not mean that tapping outside automatically dismisses it.

### Question 2: Is session storage a reasonable way to carry information between steps of a multi-step dialog flow?

**Answer: True**

**Explanation:** Session storage can retain information, such as the current username, between steps without passing it through every function's arguments.

### Question 3: What is an `AlertDialog` generally used for?

**Answer: B — Interrupting the user with a modal message or short interaction, without leaving the current screen.**

**Explanation:** An `AlertDialog` displays important messages, confirmation prompts, or short interactions.

### Question 4: Which pair of calls shows a dialog and later closes it?

**Answer: A — `page.open()` and `page.close()`**

**Explanation:** In the Flet API used by this quiz, `page.open(dialog)` opens the dialog, and `page.close(dialog)` closes it.

### Question 5: Can a dialog's content and actions be changed after it is created?

**Answer: True**

**Explanation:** Dialog content and actions can be updated to support multi-step processes, such as confirming a username before setting a new password.

### Question 6: Why should a function check a username against existing records rather than trusting the value entered earlier?

**Answer: C — To confirm the value still refers to a real, existing record before acting on it.**

**Explanation:** Checking the record helps ensure that the application acts on a valid user before performing an operation, such as updating a password.

### Question 7: When reading data from a JSON file into Python, which pair of steps is correct?

**Answer: C — Open the file in read mode, then call `json.load()` to parse its contents into a Python object.**

**Example:**

```python
import json

with open("users.json", "r") as file:
    users = json.load(file)
```

**Explanation:** `json.load()` reads JSON data from a file and converts it into a Python object, such as a dictionary or list.

### Question 8: Does splitting a login flow and a reset-password dialog into separate functions or modules make the code harder to reuse and maintain?

**Answer: False**

**Explanation:** Separating responsibilities generally improves code organisation, reusability, readability, and maintainability.

### Question 9: Why validate and display an error at each step of a multi-step dialog flow?

**Answer: D — It gives the user immediate feedback and prevents the flow from advancing on invalid or incomplete input.**

**Explanation:** Step-by-step validation helps users correct mistakes before proceeding to the next stage.

### Question 10: After changing a Python dictionary loaded from a JSON file, what must happen for the change to persist the next time the app runs?

**Answer: A — The updated data must be written back to the file, typically with `json.dump()`.**

**Example:**

```python
import json

users = {"username": "Alex", "active": True}

users["active"] = False

with open("users.json", "w") as file:
    json.dump(users, file, indent=4)
```

**Explanation:** Changing a dictionary updates data in memory only. Writing the updated dictionary back to the JSON file saves the change permanently.

## Key Concepts Learned

- **Modal dialogs:** Display messages or interactions while blocking the underlying screen.
- **Session storage:** Carry information between steps of a user flow.
- **Dialog management:** Open, close, and update dialog controls.
- **Input validation:** Validate each step before allowing the user to continue.
- **User verification:** Check records before performing sensitive operations.
- **JSON reading:** Use `json.load()` to read and parse JSON files.
- **JSON writing:** Use `json.dump()` to save updated data to a file.
- **Modular programming:** Separate application functions to improve maintainability.

## Conclusion

This quiz reinforces the importance of building secure, organised, and user-friendly Flet applications. It also demonstrates how to manage dialogs, validate user input, verify records, and persist data using JSON files.
