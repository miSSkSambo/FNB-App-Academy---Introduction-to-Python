# Flet Summative Quiz – 20 Questions and Answers

## Overview

This quiz covers essential concepts in Python and the Flet framework, including UI layouts, routing, styling, dialogs, event handling, client storage, virtual environments, and control properties.

## Questions and Answers

### Question 1: Why should `page.views` be cleared before appending a new route's view?

**Answer: A — Without clearing, old views stack up underneath, so back navigation could behave unpredictably or show stale screens.**

**Explanation:** Clearing the view list helps keep the displayed view stack consistent with the current route.

### Question 2: What is the key difference between padding and margin on a Container?

**Answer: C — Padding adds space inside the container's border; margin adds space outside it, between the container and its neighbours.**

**Explanation:** Padding controls internal spacing, while margin controls external spacing.

### Question 3: Which TextField property would restrict the on-screen keyboard to a numeric layout on mobile?

**Answer: C — `keyboard_type`.**

**Explanation:** This is the expected answer from the quiz options. The exact property name for numeric keyboard configuration depends on the Flet version.

### Question 4: Can a Flet app built in Python potentially run as a desktop, web, or mobile app without rewriting its UI code for each platform?

**Answer: True.**

**Explanation:** Flet supports building applications for multiple platforms using Python.

### Question 5: Is assigning a control to a variable necessary if you need to read or update its properties later from a function?

**Answer: True.**

**Explanation:** A variable provides a reference to the control so its properties can be accessed and changed later.

### Question 6: Is changing a control's property in code enough on its own to make the change appear on screen?

**Answer: False.**

**Explanation:** In the usual Flet workflow, call `.update()` on the control or an appropriate parent/page to reflect the change.

### Question 7: Should a project's virtual environment folder, such as `venv`, typically be committed to Git?

**Answer: False.**

**Explanation:** Virtual environments should normally be excluded through `.gitignore`. Dependencies can be recreated from `requirements.txt` or `pyproject.toml`.

### Question 8: What call is required after a route-change handler builds and appends the matching view?

**Answer: A — `page.update()`.**

**Explanation:** Updating the page refreshes the interface to reflect the changes to its views.

### Question 9: Can a route-change handler check `page.session` and redirect to `/login` if the user is not authenticated?

**Answer: True.**

**Explanation:** This is a common approach to protecting screens that require authentication.

### Question 10: What is the Container control mainly used for?

**Answer: C — Wrapping a control to apply background colour, padding, borders, sizing, and alignment.**

**Explanation:** A Container groups a control and allows its appearance and layout to be configured.

### Question 11: Which control visually separates sections of a form with a thin horizontal line?

**Answer: B — Divider.**

**Explanation:** A Divider creates a visual separation between sections of an interface.

### Question 12: Are preferences stored by one unrelated Flet app generally isolated from another app?

**Answer: True.**

**Explanation:** Flutter applications generally have separate preferences storage, so one app's values are isolated from another's.

### Question 13: Which event fires when text inside a TextField changes?

**Answer: C — `on_change`.**

**Explanation:** The `on_change` event can be used for live validation as the user types.

### Question 14: Does a route-change handler typically clear the page's view list before appending the view for the new route?

**Answer: True.**

**Explanation:** Clearing and rebuilding the view list helps ensure that the appropriate screen is displayed.

### Question 15: Is `page.route` limited to the last segment typed by the user?

**Answer: False.**

**Explanation:** A route can include multiple path segments, such as `/product/42`, which the handler can parse to identify the requested screen or resource.

### Question 16: Which layout control stacks child controls vertically?

**Answer: A — Column.**

**Explanation:** A Column arranges its children vertically, one below another.

### Question 17: Can a dialog's content and actions be changed after creation to support a multi-step flow?

**Answer: True.**

**Explanation:** Updating dialog content and actions can support workflows such as confirmation followed by data entry.

### Question 18: What is the purpose of setting a custom value on a control's `data` property?

**Answer: A — It attaches arbitrary custom data to the control, retrievable in the handler via `e.control.data`.**

**Example:**

```python
ft.ElevatedButton(
    "Delete",
    data=item_id,
    on_click=handle_delete
)
```

**Explanation:** The event handler can access the stored item ID through the control's `data` property.

### Question 19: Do Checkbox and Slider controls both support an `on_change` event?

**Answer: True.**

**Explanation:** Both controls can trigger `on_change` when their values change.

### Question 20: What happens when `opacity=0.5` is set on a Container wrapping the entire login form?

**Answer: A — It makes the entire container, including its content, semi-transparent.**

**Explanation:** An opacity value of `0.5` makes the container and its rendered content approximately 50% opaque.

## Key Concepts Learned

- **Layouts:** Use Column, Row, Container, and Divider to organise interfaces.
- **Routing:** Manage screens using routes and view lists.
- **Styling:** Apply padding, margin, opacity, and other visual properties.
- **Event handling:** Respond to user actions using events such as `on_change`.
- **Dialogs:** Update dialog content and actions for multi-step interactions.
- **Custom data:** Attach values to controls using the `data` property.
- **Client storage:** Persist small values between app sessions.
- **Session management:** Check authentication before showing protected screens.
- **Git version control:** Exclude virtual environments and track dependency files.
- **UI updates:** Refresh the interface after changing control properties.

## Conclusion

This quiz reinforces the fundamentals of developing interactive Flet applications. Understanding layouts, styling, routing, storage, events, and UI updates helps developers build applications that are organised, maintainable, and user-friendly.
