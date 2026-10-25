# Unit 5: APIs – Quiz 1 Questions and Answers

## Overview

This quiz introduces the fundamentals of Application Programming Interfaces (APIs), REST architecture, HTTP methods, status codes, and JSON data. These concepts help developers connect Python and Flet applications to external services and real-world data.

## Questions and Answers

### Question 1: As defined in the lesson, what is an API?

**Answer: B — A set of defined rules that let two or more software applications communicate with one another.**

**Explanation:** APIs allow applications to exchange information and use each other's functionality.

### Question 2: In the key/value analogy from the lesson, what does the "value" represent?

**Answer: A — The meaning associated with the keyword.**

**Explanation:** In a key-value pair, the key identifies an item, while the value contains the information associated with that key.

### Question 3: What does API stand for?

**Answer: B — Application Programming Interface.**

**Explanation:** An API defines how different software components communicate and interact.

### Question 4: What does an HTTP 200 status code mean?

**Answer: A — The request was successful.**

**Explanation:** HTTP status code `200 OK` indicates that a request succeeded.

### Question 5: What does REST stand for?

**Answer: C — Representational State Transfer.**

**Explanation:** REST is an architectural style commonly used to design web APIs.

### Question 6: What kind of object does a WebSocket API use to structure its data?

**Answer: D — JSON object.**

**Explanation:** JSON is commonly used to structure data exchanged through WebSocket connections, although WebSockets can transmit other data formats as well.

### Question 7: What protocol does a REST API use to send requests between client and server?

**Answer: D — HTTP.**

**Explanation:** REST APIs commonly use HTTP methods to request, create, update, and delete resources.

### Question 8: Which HTTP method creates a new resource in the database?

**Answer: C — POST.**

**Explanation:** The `POST` method is commonly used to submit data that creates a new resource.

### Question 9: Which HTTP method removes an existing resource from the database?

**Answer: B — DELETE.**

**Explanation:** The `DELETE` method requests the removal of a specified resource.

### Question 10: Which option was NOT given as one of the three reasons APIs matter?

**Answer: B — Real-time video encoding.**

**Explanation:** The listed reasons were hiding code complexity from users, task automation, and system integration.

## Key Concepts Learned

- **API:** Enables communication between software applications.
- **Key-value pairs:** Connect a key to its associated value.
- **REST:** An architectural style for web services.
- **HTTP status codes:** Communicate the result of a request.
- **JSON:** A common format for exchanging structured data.
- **HTTP methods:** `GET`, `POST`, `PUT`, and `DELETE` support common resource operations.
- **System integration:** APIs connect different applications and services.
- **Task automation:** APIs allow applications to perform actions automatically.

## Conclusion

This quiz builds a foundation for connecting Python and Flet applications to external services. Understanding APIs, REST, HTTP methods, status codes, and JSON is essential when retrieving and displaying real-world data.

## Suggested Practical Activity

Create a Python program using the `requests` library to retrieve data from a public REST API. Parse the JSON response and display selected values in the terminal. Then extend the program to show the results in a Flet interface.
