# Unit 6: Build Sprint, Peer Testing and Software Development — 50 Questions and Answers

## Overview

This README contains 50 questions and answers covering Python application development, Flet, debugging, peer testing, software design, project organisation, and iterative development.

**Topics covered:**
- Build Sprint planning and development
- Peer testing and usability
- UI design and consistency
- Flet navigation and controls
- Object-oriented programming
- JSON data persistence
- Debugging and error handling
- GitHub project structure and documentation
- Iterative software development

---

## Questions and Answers

### Q1. What are the five stages of the software development process?
**Answer:** A — Plan, design, build, test, iterate.

**Explanation:** These stages help developers organise their work and improve the application through repeated testing.

### Q2. Why can peer testing identify issues that the developer may miss?
**Answer:** B — Peers do not have the developer's built-in assumptions and can identify confusing labels or workflows.

**Explanation:** Fresh users interact with an application differently from the person who created it.

### Q3. What is the best approach to peer testing?
**Answer:** A — Explain the purpose, observe silently, and record hesitation or difficulties.

**Explanation:** Avoid guiding the tester so that you can observe how intuitive the application really is.

### Q4. Why should polishing come after core functionality?
**Answer:** C — Polishing a broken feature wastes time.

**Explanation:** The application should work correctly before time is spent improving its appearance.

### Q5. How should a shared accent colour be managed in Flet?
**Answer:** B — Define it once using `page.theme`.

**Explanation:** Centralised theme settings promote consistency and make future changes easier.

### Q6. What contributes to the perceived quality of an application?
**Answer:** A — Consistent spacing and padding.

**Explanation:** Consistent layouts make an application appear more professional and easier to use.

### Q7. Why should icons be accompanied by text labels?
**Answer:** D — Icons can be ambiguous, especially for users who are less familiar with technology.

**Explanation:** Text labels clarify the purpose of buttons and other controls.

### Q8. What should a completed capstone submission include beyond code?
**Answer:** B — An organised folder structure and a README explaining the application and how to run it.

**Explanation:** These materials help assessors and other developers understand the project.

### Q9. Why is a README important?
**Answer:** A — It allows someone unfamiliar with the project to understand and run it without asking for help.

**Explanation:** Good documentation explains the application's purpose, setup, and usage.

### Q10. What is the purpose of a mid-week checkpoint?
**Answer:** C — To have a working prototype ready for peer testing before the final deadline.

**Explanation:** Early testing provides time to address problems before submission.

### Q11. What is the risk of polishing before implementing core logic?
**Answer:** A — Time is spent improving an application before its functionality exists.

**Explanation:** Functional requirements should be prioritised before decorative improvements.

### Q12. What is the risk of testing only at the end?
**Answer:** B — Problems may be discovered too late to fix properly.

**Explanation:** Testing throughout development reduces the risk of last-minute failures.

### Q13. What does a Python traceback show?
**Answer:** D — The chain of function calls that led to an error.

**Explanation:** Reading a traceback helps identify the location and cause of a problem.

### Q14. Why should peer feedback be documented?
**Answer:** A — It records user feedback and demonstrates how the application was refined.

**Explanation:** Written feedback helps developers prioritise and justify improvements.

### Q15. What is a good project folder structure?
**Answer:** B — `main.py`, supporting modules, data or assets, and a README.

**Explanation:** A clear structure makes code easier to maintain and navigate.

### Q16. What is the risk of ignoring an early bug report?
**Answer:** B — Problems may compound and become more difficult to resolve.

**Explanation:** Investigating issues early helps prevent additional problems.

### Q17. What is the objective of time management during a Build Sprint?
**Answer:** A — Balance building, testing, and polishing within the available time.

**Explanation:** Real-world development requires prioritisation and effective use of limited time.

### Q18. What is an example of clean application architecture?
**Answer:** D — Separating data models, persistence, and UI view-building.

**Explanation:** Separation of responsibilities makes code easier to test, reuse, and maintain.

### Q19. What should you do if users repeatedly tap the wrong button?
**Answer:** C — Reconsider the button's label and layout.

**Explanation:** Repeated mistakes may indicate a usability problem rather than user error.

### Q20. Why is software development often described as a loop?
**Answer:** B — Build, test, and iterate repeatedly.

**Explanation:** Each development cycle provides opportunities to identify and fix problems.

### Q21. Why is a README containing only “This is my app” insufficient?
**Answer:** B — It lacks a meaningful explanation and instructions for running the application.

**Explanation:** Documentation should give readers enough information to understand and use the project.

### Q22. What should happen after testing reveals a bug?
**Answer:** D — Iterate by fixing or improving the application, then test again.

**Explanation:** A fix should be followed by further testing to verify the result.

### Q23. How should you investigate a crash that occurs when `notes.json` is empty?
**Answer:** B — Create a minimal test case that loads an empty JSON file.

**Explanation:** A small reproducible test helps isolate the cause of the failure.

### Q24. Why should you avoid explaining every step while a peer tests your application?
**Answer:** C — Explaining the application can hide the confusion experienced by a first-time user.

**Explanation:** Silent observation reveals whether the interface communicates its purpose clearly.

### Q25. Why should an `Expense` class be separate from a Flet view?
**Answer:** B — The model can be tested and reused independently of the interface.

**Explanation:** Separating business logic from the UI improves maintainability and testability.

### Q26. What should you do if the Add Expense button blends into the background?
**Answer:** D — Improve the UI's contrast and the button's visual prominence.

**Explanation:** Important actions should be easy to identify.

### Q27. What is the difference between a Week 3 design brief and a Week 8 Build Sprint?
**Answer:** D — The Build Sprint translates the validated design into working code.

**Explanation:** Design establishes the intended solution; the Build Sprint implements it.

### Q28. What makes peer feedback notes meaningful?
**Answer:** A — They provide evidence that real user feedback was collected and considered.

**Explanation:** Documenting observations helps demonstrate user-centred development.

### Q29. If you have one day remaining, should you fix a data-saving bug or add a decorative animation?
**Answer:** B — Fix the data-saving bug.

**Explanation:** Core functionality and data integrity take priority over decorative features.

### Q30. Which is an unhelpful debugging technique?
**Answer:** D — Randomly changing unrelated parts of the code.

**Explanation:** Systematic debugging focuses on the cause of the error instead of making arbitrary changes.

### Q31. What does a project containing `main.py`, `models.py`, a data folder, and a README demonstrate?
**Answer:** C — Good packaging and easy navigation for the assessor.

**Explanation:** Organised files make the project easier to understand and evaluate.

### Q32. What is iterative development?
**Answer:** C — Repeated testing and refinement rather than relying on a single attempt.

**Explanation:** Developers improve their work through multiple cycles of feedback and testing.

### Q33. How can skills learned throughout the course be integrated?
**Answer:** B — Combine a class model, persistent data, and a themed multi-view UI where appropriate.

**Explanation:** This integrates object-oriented programming, storage, and interface design.

### Q34. What is the risk of skipping a mid-week checkpoint?
**Answer:** A — Usability issues may be discovered too late.

**Explanation:** A checkpoint provides an opportunity to collect feedback while there is still time to improve the application.

### Q35. What is the difference between design and building?
**Answer:** A — Design finalises the data model and screens, while building implements them in code.

**Explanation:** A clear design provides a plan for implementation.

### Q36. What can happen if a developer skips the checkpoint?
**Answer:** C — Usability issues may remain undetected until the final stage, leaving insufficient time to fix them.

**Explanation:** Early validation reduces late-stage risk.

### Q37. How can you investigate a problem in one feature?
**Answer:** B — Test the smallest reproducible part of the feature.

**Explanation:** Isolating the problem reduces distractions and helps identify the cause.

### Q38. What does an application with a `Task` class, `tasks.json`, and themed Home/Add-Task views demonstrate?
**Answer:** C — Integration of object-oriented programming, file persistence, and multi-view UI development.

**Explanation:** These components combine several important programming concepts.

### Q39. What should you do when a peer says a button's purpose is unclear?
**Answer:** A — Treat the feedback as a genuine usability signal and clarify the label or add a helpful text hint.

**Explanation:** User feedback can reveal problems that the developer did not notice.

### Q40. Why should planning happen before building?
**Answer:** D — Building without confirming the plan risks creating the wrong solution.

**Explanation:** Planning clarifies requirements and priorities before implementation begins.

### Q41. What does it mean to iterate?
**Answer:** D — Repeatedly improve the application based on testing and feedback.

**Explanation:** Iteration creates a cycle of building, testing, and refining.

### Q42. What should you do if the application works but its padding is inconsistent?
**Answer:** C — Address the inconsistency during the polish stage.

**Explanation:** Once functionality is stable, visual consistency can be improved.

### Q43. Why keep data and assets in separate folders?
**Answer:** A — To keep code, data, and resources organised.

**Explanation:** Separating files makes projects easier to maintain.

### Q44. What does an expense tracker with a class, JSON storage, and Home/History views demonstrate?
**Answer:** C — Object-oriented programming, persistent storage, and a multi-view UI.

**Explanation:** The design integrates data modelling, saving information, and navigation.

### Q45. What is the risk of fixing a bug without retesting?
**Answer:** D — The fix might not resolve the issue or could introduce another bug.

**Explanation:** Retesting verifies that the change works as intended.

### Q46. What is a useful first step when debugging a traceback?
**Answer:** B — Read the traceback from the bottom up to identify the exception type and error location.

**Explanation:** The final lines usually contain the most specific error message.

### Q47. What does the last line of a Python traceback usually show?
**Answer:** D — The exception type and error message.

**Explanation:** This line describes the error that caused the program to fail.

### Q48. How can `print()` help with debugging?
**Answer:** B — Temporarily display variable values at specific points in the code.

**Explanation:** Print debugging helps confirm what data the program receives and how values change.

### Q49. Why is a smallest reproducible example useful?
**Answer:** D — It removes unrelated distractions and helps isolate the problem.

**Explanation:** A minimal example makes errors easier to reproduce and investigate.

### Q50. Which is a good example of print debugging in practice?
**Answer:** A — Temporarily add a `print()` statement to confirm what value was received before an error occurs.

**Explanation:** Inspecting the actual value can reveal unexpected input or incorrect assumptions.

---

## Key Lessons

1. **Plan before coding:** Confirm the requirements and intended design.
2. **Build core functionality first:** Ensure the main features work before polishing.
3. **Test early and often:** Discover problems while there is time to fix them.
4. **Use peer feedback:** Observe real users and document their difficulties.
5. **Debug systematically:** Read tracebacks, inspect values, and create minimal reproducible examples.
6. **Keep code organised:** Separate models, persistence, and interface components.
7. **Document your project:** Include a useful README and clear run instructions.
8. **Iterate continuously:** Improve the application through repeated build-test-refine cycles.

## Suggested Repository Structure

```text
unit-6-build-sprint-quiz/
├── README.md
├── main.py
├── models.py
├── data/
└── assets/
```

*Note: The folders and Python files above are an example structure for a project. For a quiz-only repository, the README.md file may be sufficient.*

## Purpose

This resource is intended for revision and study of Unit 6 concepts, including application development, usability testing, debugging, project organisation, and iterative improvement.




<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/c1b25867-cc97-42a1-8c31-4791e2e95b97" />
