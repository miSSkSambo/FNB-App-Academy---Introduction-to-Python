REST API PUT and DELETE Requests – Quiz Questions and Answers

## Overview

This quiz covers updating and deleting resources using REST APIs in Python. It focuses on the HTTP methods `GET`, `POST`, `PUT`, and `DELETE`, identifying individual resources by ID, maintaining consistent JSON data, and handling HTTP errors.

## Questions and Answers

### Question 1: After deleting a song, what happens when you GET that same song again?

**Answer: C — It returns an HTTP error because the song can no longer be found.**

**Explanation:** If the resource has been successfully deleted, requesting its ID again will commonly return `404 Not Found`.

### Question 2: How do you write a multi-line comment in Python, as shown in the video?

**Answer: D — Open and close the block with triple double-quotes (`"""`).**

**Explanation:** Triple-quoted strings are commonly used for multi-line text and docstrings. Python does not have a dedicated multi-line comment syntax; for comments, use `#` on each line.

### Question 3: How is one specific song targeted for a PUT or DELETE request?

**Answer: A — The song's ID appended to the base URL as a path segment (e.g. `/1`).**

**Example:**

```python
url = "https://example.com/api/songs/1"
```

**Explanation:** The ID identifies the individual resource to update or delete.

### Question 4: What data-consistency mistake from the previous lesson gets fixed first?

**Answer: D — Making sure every field's value is a string.**

**Explanation:** Consistent data types make records easier to process and display, provided strings are the required types for the lesson's fields.

### Question 5: What do lessons 3 and 4 demonstrate together?

**Answer: B — Performing GET, POST, PUT, and DELETE requests against a REST API with Python's `requests` library.**

**Explanation:** These HTTP methods allow an application to retrieve, create, replace, and delete API resources.

### Question 6: What field-name typo do they find and correct in the song data?

**Answer: B — `"name"` should be `"title"`.**

**Explanation:** Consistent field names help ensure that the application accesses the correct data properties.

### Question 7: Which requests function removes an existing resource from the database?

**Answer: A — `requests.delete()`.**

**Example:**

```python
import requests

response = requests.delete(
    "https://example.com/api/songs/1"
)
response.raise_for_status()
```

**Explanation:** The DELETE method requests the removal of the specified resource.

### Question 8: Which requests function replaces an existing resource entirely?

**Answer: A — `requests.put()`.**

**Example:**

```python
import requests

url = "https://example.com/api/songs/1"

updated_song = {
    "title": "Never Let Me Down",
    "artist": "Kanye West"
}

response = requests.put(url, json=updated_song)
response.raise_for_status()
```

**Explanation:** PUT is commonly used to replace a resource with the supplied representation. The exact behaviour depends on the API.

### Question 9: Which song gets replaced with "Never Let Me Down"?

**Answer: B — Through The Wire.**

**Explanation:** This is the answer indicated by the quiz options for the lesson demonstration.

### Question 10: Which song ID is deleted in this lesson?

**Answer: C — ID 1.**

**Explanation:** This is the answer indicated by the quiz options for the lesson demonstration.

## Key Concepts Learned

- **GET:** Retrieve a resource from an API.
- **POST:** Create a new resource.
- **PUT:** Replace an existing resource.
- **DELETE:** Remove an existing resource.
- **Resource IDs:** Identify individual records using URL path segments.
- **JSON consistency:** Use consistent field names and data types.
- **HTTP errors:** Handle unsuccessful requests using `raise_for_status()`.
- **Python requests:** Communicate with REST APIs through HTTP methods.

## Conclusion

This quiz reinforces the fundamentals of modifying API data using Python's `requests` library. Understanding how to retrieve, create, replace, and delete resources is essential when connecting Flet applications to external data services.

## Suggested Practical Activity

Using a mock REST API:

1. Retrieve all songs with `requests.get()`.
2. Create a new song with `requests.post()`.
3. Replace an existing song using `requests.put()`.
4. Delete a song using `requests.delete()`.
5. Try retrieving the deleted song and handle the resulting HTTP error.
