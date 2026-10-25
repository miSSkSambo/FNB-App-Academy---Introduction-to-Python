# Flet Navigation and Routing Quiz – Questions and Answers

## Overview

This quiz covers navigation and routing in Python using the Flet framework. It focuses on switching between screens, handling route changes, managing user sessions, implementing logout, and organising application code into separate modules.

## Questions and Answers

### Question 1: Which call is used to navigate the user to a different route or screen from within the app, such as after a successful login?

**Answer: E — `page.push_route("/home")`**

**Explanation:** This is the expected answer from the quiz options. The exact navigation API depends on the Flet version. In versions that support route assignment, `page.route = "/home"` can also be used.

### Question 2: A route-change handler typically clears `page.views` before appending the view that matches the new route.

**Answer: True**

**Explanation:** Clearing the views before adding the appropriate screen helps ensure that the correct view is displayed for the current route.

### Question 3: What is the purpose of the final `else` branch in a route-change handler?

**Answer: B — It provides a sensible fallback view, such as the login page, for any route that doesn't match a known screen.**

**Explanation:** A fallback prevents the application from being left without a suitable screen when an unknown route is requested.

### Question 4: What does each `ft.View` represent in a multi-view app?

**Answer: D — One distinct screen, identified by a route string.**

**Explanation:** Each `ft.View` represents a screen, such as the login, registration, or home page.

### Question 5: Which property is checked inside a route-change handler to decide which `ft.View` should be built and shown?

**Answer: A — `page.route`**

**Explanation:** The route identifies the current screen, allowing the application to build and display the appropriate view.

### Question 6: Is removing the user from session storage and navigating back to `/login` a reasonable way to implement logout?

**Answer: True**

**Explanation:** Removing the stored user information clears the application's session state, and navigating to the login screen ends the current logged-in flow. Protected routes should also verify that a valid session exists.

### Question 7: If `page.push_route()` is asynchronous, can it be called directly inside a normal synchronous `on_click` handler without awaiting or scheduling it?

**Answer: True — the statement is correct.**

**Explanation:** If the method is asynchronous in the Flet version being used, it must be awaited or scheduled appropriately. Calling an asynchronous function without awaiting or scheduling it may prevent the intended operation from executing.

### Question 8: Why does `main.py` import page functions such as `login_page`, `home_page`, and `register_page` rather than defining all the UI inside `main()`?

**Answer: C — It keeps each screen's UI and logic in its own module, and `main.py` wires them together through routing.**

**Explanation:** Separating screens into modules improves code organisation, readability, reuse, and maintainability.

### Question 9: What is `page.on_route_change` used for?

**Answer: A — Registering the function that runs automatically whenever the route changes, so the correct view can be shown.**

**Explanation:** The route-change handler responds to navigation events and updates the displayed screen.

### Question 10: Does splitting an app into separate functions, each returning its own `ft.View`, make the codebase easier to navigate and maintain?

**Answer: True**

**Explanation:** Separating the login, home, and registration screens into individual functions makes the code easier to understand, test, debug, and maintain.

## Key Concepts Learned

- **Routing:** Identifies which screen should be displayed.
- **`ft.View`:** Represents a distinct screen in the application.
- **`page.route`:** Identifies the current route.
- **`page.on_route_change`:** Handles route changes and displays the appropriate view.
- **Session management:** Stores and removes user information during login and logout.
- **Fallback routes:** Provide a default screen for unknown routes.
- **Modular programming:** Separates screen logic into individual functions and modules.
- **Asynchronous functions:** Require appropriate awaiting or scheduling when the API is asynchronous.

## Conclusion

This quiz reinforces the fundamentals of building multi-screen Flet applications. Understanding routing, session management, event handling, and modular programming helps developers create applications that are organised, secure, and easier to maintain.
