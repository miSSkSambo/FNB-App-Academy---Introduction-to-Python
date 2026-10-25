REST API Requests with Python – Quiz Questions and Answers

## Overview

This quiz covers working with REST APIs in Python using the `requests` library. It focuses on GET and POST requests, JSON payloads, HTTP status codes, response parsing, and exception handling.

## Questions and Answers

### Question 1: How is the JSON payload attached to a POST request with the requests library?

**Answer: C — Via the `json=` argument of `requests.post()`.**

**Example:**

```python
import requests

url = "https://example.com/api/songs"

song = {
    "title": "New Song",
    "artist": "Example Artist"
}

response = requests.post(url, json=song)
```

**Explanation:** The `json=` argument serialises the Python dictionary into JSON and sends it as the request body.

### Question 2: What is the name of the new song added via POST in this lesson?

**Answer: A — We Don't Care.**

**Explanation:** This is the answer indicated by the quiz options for the lesson demonstration.

### Question 3: What method converts the API's response body into a usable Python object?

**Answer: D — `.json()`**

**Example:**

```python
data = response.json()
```

**Explanation:** The `.json()` method parses a JSON response into Python objects, such as dictionaries and lists.

### Question 4: What method, called on the response, automatically raises an exception for a failed request?

**Answer: D — `raise_for_status()`**

**Example:**

```python
response.raise_for_status()
```

**Explanation:** This method raises an `HTTPError` when the response has an unsuccessful HTTP status code, generally 4xx or 5xx.

### Question 5: What status code came back when the API URL was deliberately mistyped?

**Answer: C — `404`.**

**Explanation:** HTTP `404 Not Found` means the requested resource or endpoint could not be found.

### Question 6: What status code confirms a resource was successfully created?

**Answer: A — `201`.**

**Explanation:** HTTP `201 Created` indicates that a request successfully created a resource.

### Question 7: Which exception class is used to catch HTTP errors from the requests library?

**Answer: A — `requests.exceptions.HTTPError`.**

**Example:**

```python
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)
```

**Explanation:** This exception can be caught when `raise_for_status()` detects an unsuccessful HTTP response.

### Question 8: Which Python construct catches the exception from `raise_for_status()`?

**Answer: B — `try / except`.**

**Explanation:** The `try` block contains code that might raise an exception, while the `except` block handles the error.

### Question 9: Which requests function creates a new resource on the API?

**Answer: A — `requests.post()`.**

**Explanation:** The POST method is commonly used to submit data to create a new resource.

### Question 10: Which requests function sends a GET request to the API?

**Answer: C — `requests.get()`.**

**Explanation:** GET requests retrieve data from an API without normally creating or modifying resources.

## Key Concepts Learned

- **GET requests:** Retrieve information from an API.
- **POST requests:** Submit data to create a resource.
- **JSON payloads:** Send structured data using the `json=` argument.
- **Response parsing:** Use `.json()` to convert JSON responses into Python objects.
- **HTTP status codes:** Understand responses such as `200`, `201`, and `404`.
- **Error handling:** Use `raise_for_status()` and `try / except`.
- **HTTP exceptions:** Catch request failures using `requests.exceptions.HTTPError`.

## Conclusion

This quiz builds practical knowledge of connecting Python applications to REST APIs. Understanding HTTP requests, JSON payloads, status codes, and exception handling helps developers create more reliable applications.

## Suggested Practical Activity

Create a Python program that retrieves songs from a mock REST API, adds a new song using `requests.post()`, and handles unsuccessful responses using `raise_for_status()` and `try / except`.
