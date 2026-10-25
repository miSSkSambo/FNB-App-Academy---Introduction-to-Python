 Working with Mock REST APIs – Quiz Questions and Answers

## Overview

This quiz covers creating and managing a mock REST API using MockAPI.io, understanding JSON objects and key-value pairs, validating JSON data, and using Python's `requests` library to communicate with APIs.

## Questions and Answers

### Question 1: How do you view the created data as a formatted JSON page?

**Answer: B — Click the resource name (e.g. `songs`) to open its data page.**

**Explanation:** Clicking the resource name displays the data stored in that endpoint, usually in JSON format.

### Question 2: How many songs are added to the resource by the end of the video?

**Answer: D — Five.**

**Explanation:** According to the quiz answer, five songs are added to the resource during the demonstration.

### Question 3: In the key-value analogy, what does the "key" represent?

**Answer: A — The keyword being looked up.**

**Explanation:** A key identifies a specific value in a key-value pair.

### Question 4: What data type is every field value set to, for consistency?

**Answer: C — String.**

**Explanation:** Strings represent text data and are commonly used for fields such as song titles, artists, and genres.

### Question 5: What does MockAPI.io show when the entered JSON is malformed?

**Answer: D — An "Invalid JSON" message, without saying exactly what's wrong.**

**Explanation:** Invalid JSON syntax can prevent the platform from accepting the submitted data.

### Question 6: What is the example project named in the video?

**Answer: D — College Dropout.**

**Explanation:** This is the project name identified in the quiz.

### Question 7: What resource (endpoint) name is created to hold the data?

**Answer: B — `songs`.**

**Explanation:** The `songs` resource holds the song records and provides an endpoint for accessing them.

### Question 8: When adding more than one JSON object to a resource, what must they be wrapped in?

**Answer: C — An array (square brackets).**

**Example:**

```json
[
  {
    "title": "Song One",
    "artist": "Artist One"
  },
  {
    "title": "Song Two",
    "artist": "Artist Two"
  }
]
```

**Explanation:** A JSON array uses square brackets `[]` to contain multiple objects separated by commas.

### Question 9: Which platform is used to create a free mock REST API for practice?

**Answer: B — MockAPI.io.**

**Explanation:** MockAPI.io lets developers create mock endpoints for practising API requests without building a complete backend.

### Question 10: Which Python library is installed to send and receive requests from the live API?

**Answer: B — `requests`.**

**Explanation:** The `requests` library allows Python programs to send HTTP requests and process server responses.

**Installation command:**

```bash
python -m pip install requests
```

## Key Concepts Learned

- **Mock REST APIs:** Simulate API endpoints for development and testing.
- **Resources and endpoints:** Organise and access data through API URLs.
- **JSON objects:** Store related information as key-value pairs.
- **JSON arrays:** Group multiple objects in a single list.
- **JSON validation:** Ensure data follows valid JSON syntax.
- **Python requests:** Send HTTP requests to external services.
- **API responses:** Retrieve and process data returned by a server.

## Conclusion

This quiz introduces the basic workflow for creating a mock API, structuring data in JSON, and preparing to connect a Python or Flet application to an external service.

## Suggested Practical Activity

Create a `songs` resource in MockAPI.io with at least five song records. Use Python's `requests` library to retrieve the records and print each song's title and artist in the terminal.
