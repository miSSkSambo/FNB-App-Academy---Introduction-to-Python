# Flet Unit 4 Summative Assessment – 20 Questions and Answers

## Overview

This quiz covers essential concepts in Python Flet application development, including multi-screen navigation, routing, UI styling, session storage, client storage, dialogs, and state management.

## Questions and Answers

### Question 1: What does an `ft.View` represent in a Flet app?

**Answer: B — A single screen, identified by a route string.**

**Explanation:** Each `ft.View` represents a screen, such as a login, home, or quiz page.

### Question 2: Why is `page.go(page.route)` commonly called near the end of `main()`?

**Answer: D — To trigger the initial route change and display the very first screen.**

**Explanation:** It initiates navigation to the current route so the route handler can build and display the first view.

### Question 3: After clearing `page.views` and appending the correct view for the new route, what must be called to show it?

**Answer: A — `page.update()`**

**Explanation:** Updating the page refreshes the UI to reflect changes to the views.

### Question 4: What is a key advantage of Flet's approach to multi-screen navigation?

**Answer: C — Views, routes, and handlers are all plain Python, with no separate file format to keep in sync.**

**Explanation:** Flet lets developers define and connect screens using Python code.

### Question 5: What is the typical first step inside a `route_change` handler?

**Answer: C — `page.views.clear()`**

**Explanation:** Clearing the existing views allows the handler to rebuild the view stack for the current route.

### Question 6: How does Flet handle UI styling compared to frameworks with a separate styling language or file?

**Answer: C — Flet expresses styling as ordinary Python arguments on each control.**

**Explanation:** Properties such as `bgcolor`, `padding`, and `border_radius` can be configured directly in Python.

### Question 7: What does `page.views` represent?

**Answer: D — A list of `View` objects; the last one in the list is generally what is displayed.**

**Explanation:** The list represents the current view stack used for navigation.

### Question 8: Why is it good practice to separate the Home view's controls from the Quiz view's controls?

**Answer: C — It keeps the code organised and makes each screen's logic easier to read and maintain.**

**Explanation:** Separate view-building functions improve readability, testing, and maintainability.

### Question 9: Which call is used to navigate the user to a different route or screen?

**Answer: E — `page.push_route("/home")`**

**Explanation:** This is the expected answer from the original quiz options. Navigation methods can differ between Flet versions; some versions use `page.go("/home")` or route assignment.

### Question 10: How can a Container be given a background colour and padding?

**Answer:** Use `bgcolor` and `padding` properties.

```python
ft.Container(
    bgcolor="blue100",
    padding=20
)
```

**Explanation:** `bgcolor` sets the background colour, while `padding` controls the internal spacing.

### Question 11: What is the most maintainable way to keep padding and spacing consistent across every screen?

**Answer: B — Define shared constants or a theme once, and reuse them consistently across views.**

**Explanation:** Shared constants reduce duplication and make future design changes easier.

### Question 12: How does `client_storage` relate to JSON file storage?

**Answer: A — `client_storage` complements JSON files, handling small key-value settings while JSON files suit larger structured data.**

**Explanation:** Each storage method serves different needs. Choose based on the type of data and the app's requirements.

### Question 13: Which tool is appropriate for remembering a player's high score between sessions?

**Answer: B — `page.client_storage.set('high_score', score)`**

**Explanation:** Client storage can persist small values, such as settings and scores, between sessions.

### Question 14: What kind of data is `client_storage` best suited for?

**Answer: B — Small, lightweight key-value data such as settings or simple state.**

**Explanation:** It is suitable for small pieces of persistent information rather than large files.

### Question 15: Which method stores a small piece of data so it persists between app sessions in Flet?

**Answer: C — `page.client_storage.set('key', value)`**

**Explanation:** The `set()` method saves a value under a key in client storage.

### Question 16: What is a key advantage of using `page.theme` for styling?

**Answer: D — Configure the colour once via `page.theme` so it applies consistently by default.**

**Explanation:** A shared theme helps maintain consistent colours and styling throughout an application.

### Question 17: What is an `AlertDialog` generally used for?

**Answer: B — Interrupting the user with a modal message or short interaction, without leaving the current screen.**

**Explanation:** Dialogs are useful for confirmations, messages, and short interactions.

### Question 18: Which control is appropriate for confirming a reset before clearing data?

**Answer: D — `ft.AlertDialog` with Yes/No actions.**

**Explanation:** A confirmation dialog allows users to approve or cancel a potentially destructive action.

### Question 19: What should happen if an `AlertDialog` is created but never appears on screen?

**Answer: C — Call `page.open(dialog)` and/or `page.update()` as appropriate.**

**Explanation:** Creating a dialog alone may not display it. Use the dialog-opening API supported by the Flet version in use.

### Question 20: What is the most likely cause when `page.go('/quiz')` does nothing visible?

**Answer: A — The `on_route_change` handler does not have a branch that builds and appends a `View` for the `'/quiz'` route.**

**Explanation:** The route handler must recognise the route and create the corresponding view.

## Key Concepts Learned

- **Views and routes:** Build and navigate between multiple screens.
- **Route handlers:** Respond to navigation and display the correct view.
- **UI styling:** Configure controls with Python properties.
- **Themes and constants:** Reuse shared styles throughout the app.
- **Client storage:** Persist small key-value data between sessions.
- **JSON storage:** Read and
