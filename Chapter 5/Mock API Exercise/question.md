Purpose
This activity gives you hands-on practice performing all four core REST
operations, GET, POST, PUT, and DELETE, against a real HTTP API using
Python's requests library. You will create your own mock backend on
mockapi.io, then complete a partially written Python script that reads,
creates, updates, and deletes records on it.
By the end of this exercise you should be able to:
Send GET, POST, PUT, and DELETE requests with requests.
Pass data to an API using the json= parameter.
Read status_code and .json() from a response.
Handle request errors with try/except and .raise_for_status().
Build a request URL that targets a specific record by appending its
id as a path segment.
Setup
Go to mockapi.io and create a new project.
Inside your project, create a resource named Album with the
following fields, all set to type string: id, name, rate.
Pick any music album you like, it does not have to be a specific
one. Using the Data tab, manually add at least 3 songs from that
album as JSON objects, for example:
{
"id": "1",
"name": "Good Morning",
"rate": "9"
}
Open the resource page and copy its API URL.
Open mockapi.py and replace the placeholder in API_ENDPOINT with
your own URL:
API_ENDPOINT = "PASTE_YOUR_MOCKAPI_URL_HERE"
Your API_ENDPOINT must be the one you created yourself. Everyone's
mockapi.io project has a different URL, so using someone else's
endpoint (or one from a past example) will not work.
Instructions
Open mockapi.py. The GET section is already complete and working,
study it as your reference for how each request is structured. Then
complete the three TODO sections that follow it:
POST - Write the code to create a new song on the API.
PUT - Write the code to replace an existing song's data.
DELETE - Write the code to remove a song from the API.
Each TODO comment lists the exact steps to follow and the variable
names to use. Write your code directly beneath the TODO comment it
belongs to. Do not remove the TODO comments.
Running the Script
python mockapi.py
Check the printed output after each section to confirm:
GET returns your list of songs and status code 200.
POST returns status code 201 and the new song's data.
PUT returns status code 200 and the updated song's data.
DELETE returns status code 200 and the deleted song's data, and a
follow-up GET on that same id returns an HTTP error.
What to Submit
Your completed mockapi.py file.
A screenshot of the mockapi.io Data tab showing your final list of
songs after the POST, PUT, and DELETE operations have run.
