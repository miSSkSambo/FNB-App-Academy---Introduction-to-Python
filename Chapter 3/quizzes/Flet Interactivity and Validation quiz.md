# Flet Interactivity and Validation Quiz – Questions and Answers

## Overview

This quiz covers the fundamentals of interactivity and input validation in Python using the Flet framework. It focuses on event handlers, clickable controls, visibility, control variables, and updating the user interface.

## Questions and Answers

### Question 1: Why compare user input to stored values inside an event handler rather than just checking that the fields are non-empty?

**Answer:** B — To validate whether the input is correct, such as checking login credentials, before displaying feedback.

### Question 2: Which control is commonly used to make plain text or an icon clickable if you are not using a button?

**Answer:** B — `ft.GestureDetector`

**Explanation:** `GestureDetector` allows controls to respond to user gestures, such as taps.

### Question 3: Which `GestureDetector` property runs a function when its content is tapped?

**Answer:** A — `on_tap`

**Explanation:** The `on_tap` event handler executes a function when the user taps the control.

### Question 4: Which button property runs a function when the button is pressed?

**Answer:** B — `on_click`

**Explanation:** The `on_click` property connects a button press to a function.

### Question 5: What is the purpose of a TextField's helper property?

**Answer:** D — To display a small message under or near the field, such as a validation hint or error.

**Explanation:** Helper text can guide users on what to enter or explain an input requirement.

### Question 6: What does the parameter `e` represent in functions such as `login_click(e)` or `test_click(e)`?

**Answer:** D — The event object, which carries information about what happened and which control triggered it.

**Explanation:** Flet passes an event object to event-handler functions when an event occurs.

### Question 7: What happens when a control's `visible` property is set to `False` and `.update()` is called?

**Answer:** D — The control is hidden on screen, but still exists and can be shown again later.

**Explanation:** Setting `visible = False` hides a control without permanently deleting it.

### Question 8: Is assigning a control to a variable necessary if you need to read or change its properties later from a function?

**Answer:** True.

**Explanation:** Assigning a control to a variable, such as `username = ft.TextField(...)`, makes it easy to access and modify its properties later.

### Question 9: Is changing a control's property in code enough on its own to make the change appear on screen?

**Answer:** False.

**Explanation:** In the usual Flet event-handling workflow, call `.update()` on the control or an appropriate parent/page to apply the change to the displayed interface.

### Question 10: Does clearing a field's helper or error text still require calling `.update()` for the message to disappear from the screen?

**Answer:** True.

**Explanation:** After clearing the helper or error text, call `.update()` so the interface reflects the change.

## Key Concepts Learned

- **Event handlers:** Functions such as `on_click` and `on_tap` respond to user actions.
- **Gesture detection:** `ft.GestureDetector` makes controls respond to gestures.
- **Input validation:** Check that user input is correct, not merely present.
- **Control variables:** Store references to controls to access their properties later.
- **Visibility:** Use `visible = False` to hide a control without deleting it.
- **UI updates:** Use `.update()` to reflect changes in the interface.

## Conclusion

This quiz reinforces the essential skills needed to create interactive Flet applications with clickable controls, input validation, event handling, and dynamic user-interface updates.
