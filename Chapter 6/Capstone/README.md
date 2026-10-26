Live Weather Dashboard


































































A lightweight weather dashboard built with Python, Flet, and the free Open-Meteo API. The application allows users to search for a city and view current weather conditions through a clean, responsive desktop and mobile-friendly interface.

The project demonstrates how to build a practical Flet application that consumes a REST API, processes JSON data, provides visual feedback, handles network failures, and can be packaged for Android as an APK.




Contents

•
Project Overview

•
Features

•
Application Preview

•
Technology Stack

•
Languages Used

•
Project Structure

•
Requirements

•
Installation

•
Running the Application

•
Using the Dashboard

•
How the Application Works

•
API Integration

•
Error Handling

•
Testing

•
Building an Android APK

•
Troubleshooting

•
Possible Improvements

•
Data Source and Attribution

•
License




Project Overview

The Live Weather Dashboard is a capstone application that retrieves live weather data from Open-Meteo and presents it in a simple graphical interface.

The application follows this process:

1.
The user enters the name of a city.

2.
The application sends the city name to the Open-Meteo Geocoding API.

3.
The API returns the city's latitude and longitude.

4.
The application sends those coordinates to the Open-Meteo Forecast API.

5.
The current weather data is returned as JSON.

6.
The application extracts the relevant values and displays them in the Flet interface.

7.
If a request fails, the application displays a clear message instead of closing unexpectedly.

This project is suitable for demonstrating REST API usage, JSON parsing, event-driven programming, user interface design, debugging, and application packaging.




Features

Weather search

Users can enter a city name and retrieve current weather information for that location.

Current weather information

The dashboard displays:

•
City and country

•
Current temperature in degrees Celsius

•
General weather conditions

•
Weather icon

•
Feels-like temperature

•
Relative humidity

•
Wind speed in kilometres per hour

Refresh functionality

The Refresh Weather button allows the user to request updated weather data without restarting the application.

Loading feedback

A progress indicator is displayed while the application is contacting the API.

User-friendly error messages

The app handles common problems, including:

•
Empty city searches

•
Cities that cannot be found

•
Slow network requests

•
Loss of internet connectivity

•
HTTP errors returned by the API

•
Unexpected or incomplete JSON responses

No API key required

Open-Meteo provides the required geocoding and weather endpoints without requiring an API key for this educational project.

Current Flet API

The application uses the current Flet button API:

Python


ft.Button(content="Refresh Weather")



This is important for Flet 1.0 and later, where the older ft.ElevatedButton API is no longer available.




Application Preview

Add a screenshot of the running application to this section if desired:

Markdown


![Live Weather Dashboard](assets/weather-dashboard.png)



Recommended screenshot location:

Plain Text


assets/weather-dashboard.png






Technology Stack

Technology
Purpose
Python
Application programming language
Flet
User interface framework
Requests
HTTP requests to the Open-Meteo APIs
Open-Meteo
Geocoding and weather data provider
JSON
Data format returned by the APIs
PowerShell or Terminal
Running and testing the application







Languages Used

The project uses the following languages and data formats:

Language or format
Usage in this project
Python
Main application logic, Flet interface, API requests, JSON parsing, and error handling
Markdown
Project documentation in README.md
JSON
Data format returned by the Open-Meteo REST APIs
PowerShell
Windows setup, dependency installation, application execution, and APK commands




Python is the primary programming language used to build the application. Markdown, JSON, and PowerShell support the documentation, API communication, and development workflow.

Main Python libraries

•
Flet — Builds the graphical user interface and handles user interaction.

•
Requests — Sends HTTP requests to the Open-Meteo services.




Project Structure

A recommended project structure is shown below:

Plain Text


FNB-App-Academy---Introduction-to-Python/
├── .venv/
├── Capstone/
│   ├── weather_app.py
│   ├── requirements.txt
│   ├── README.md
│   └── assets/
│       └── weather-dashboard.png
├── chapter 1/
├── chapter 2/
├── chapter 3/
├── chapter 4/
└── chapter 5/



Important files

File
Description
weather_app.py
Main Flet application
requirements.txt
Python package dependencies
README.md
Project documentation
assets/
Optional screenshots, icons, and other project assets
.venv/
Local Python virtual environment; do not commit this folder




If the project is stored in a separate repository, the project folder can be simplified to:

Plain Text


weather-dashboard/
├── weather_app.py
├── requirements.txt
├── README.md
└── assets/






Requirements

Before running the application, install the following:

•
Python 3.9 or later

•
Flet

•
Requests

•
An active internet connection

The application does not require an Open-Meteo API key.




Installation

1. Open the project folder

In PowerShell, navigate to the folder containing weather_app.py:

Plain Text


cd "C:\Users\ksamb\OneDrive\Desktop\Github\FNB-App-Academy---Introduction-to-Python\Capstone"



Use the actual location of your project if it is different.

2. Create a virtual environment

A virtual environment keeps this project's dependencies separate from other Python projects.

From the project folder, run:

Plain Text


python -m venv .venv



3. Activate the virtual environment

On Windows PowerShell:

Plain Text


.\.venv\Scripts\Activate.ps1



On Windows Command Prompt:

Plain Text


.venv\Scripts\activate



On macOS or Linux:

Bash


source .venv/bin/activate



When activation is successful, the terminal normally displays (.venv) before the current path.

4. Install the dependencies

Create a file named requirements.txt with the following content:

Plain Text


flet
requests



Then install the dependencies:

Plain Text


python -m pip install -r requirements.txt



Alternatively, install the packages directly:

Plain Text


python -m pip install flet requests



5. Confirm the Flet installation

You can verify the installed version with:

Plain Text


python -m pip show flet



You can also check the Requests installation with:

Plain Text


python -m pip show requests






Running the Application

Make sure the virtual environment is active and that your terminal is inside the Capstone folder.

Run the application with:

Plain Text


python .\weather_app.py



On macOS or Linux, use:

Bash


python3 ./weather_app.py



The application loads weather data for London when it starts. The default city can be changed by editing the following line in weather_app.py:

Python


value="London",



For example:

Python


value="Cape Town",






Using the Dashboard

1.
Start the application.

2.
Enter a city name in the search field.

3.
Select Refresh Weather.

4.
Wait for the weather request to complete.

5.
Review the current temperature and weather information.

6.
Try another city to test the search functionality.

7.
Disconnect from the internet or enter an invalid city to test the error states.

The application displays a status message below the weather card. A successful request displays a confirmation message, while a failed request displays an explanation of the problem.




How the Application Works

1. City geocoding

The application first converts the city name into coordinates by calling the Open-Meteo Geocoding API.

The request includes parameters such as:

Python


{
    "name": city,
    "count": 1,
    "language": "en",
    "format": "json",
}



The first matching result is used to obtain:

•
Latitude

•
Longitude

•
Official city name

•
Country name

2. Weather request

The coordinates are then sent to the Open-Meteo Forecast API. The application requests:

•
temperature_2m

•
relative_humidity_2m

•
apparent_temperature

•
weather_code

•
wind_speed_10m

The request uses Celsius for temperature, kilometres per hour for wind speed, and the location's automatic timezone.

3. JSON parsing

The response is converted to a Python dictionary with:

Python


weather_data = weather_response.json()



The current weather section is then read:

Python


current_weather = weather_data["current"]



Individual values are extracted and inserted into the Flet controls.

4. Weather-code conversion

Open-Meteo returns numeric weather codes. The application converts these codes into readable descriptions and icons using the WEATHER_CODES dictionary.

For example:

Python


0: ("Clear sky", "☀️")
63: ("Moderate rain", "🌧️")
95: ("Thunderstorm", "⛈️")



5. Interface update

The application updates the relevant Flet controls after receiving the API response:

Python


temperature_text.value = f"{temperature:.1f}°C"
condition_text.value = condition
weather_icon.value = icon



The page is then refreshed so that the updated values appear in the interface.




API Integration

This project uses two Open-Meteo endpoints.

Geocoding API

The geocoding endpoint searches for a city and returns geographic coordinates:

Plain Text


https://geocoding-api.open-meteo.com/v1/search



Forecast API

The forecast endpoint returns weather data for a given latitude and longitude:

Plain Text


https://api.open-meteo.com/v1/forecast



Example request flow

Plain Text


User enters city
        |
        v
Geocoding API
        |
        v
Latitude and longitude
        |
        v
Forecast API
        |
        v
Current weather JSON
        |
        v
Flet weather dashboard



For further information, visit the 

Open-Meteo documentation.




Error Handling

The application uses try and except blocks to prevent network failures from crashing the interface.

Empty input

If the search field is empty, the application displays:

Plain Text


Please enter a city name.



Location not found

If the geocoding API does not return a result, the application displays:

Plain Text


Could not find a location called 'city-name'.



Timeout

If the API does not respond within the configured timeout period, the application displays a timeout message.

Connection error

If the device cannot connect to the internet or the service, the application displays a connection message.

HTTP error

If the API returns an unsuccessful HTTP response, the application displays a service error message.

Unexpected response

If the API response is missing an expected field or contains an unexpected value, the application displays a data-format message.

This approach improves the user experience by providing feedback instead of exposing a Python traceback inside the application.




Testing

Functional testing checklist




The application starts without a Python traceback.




London weather loads automatically on startup.




A valid city returns weather information.




Multiple cities can be searched successfully.




An empty input displays a useful error message.




An invalid city displays a useful error message.




The Refresh button requests new data.




The loading indicator appears during a request.




The loading indicator disappears after success or failure.




Temperature is displayed in degrees Celsius.




Humidity is displayed as a percentage.




Wind speed is displayed in kilometres per hour.




Weather conditions and icons match the returned weather code.




The interface remains readable when the window is resized.

Network testing checklist




Test with a normal internet connection.




Test while disconnected from the internet.




Test with a slow or unstable connection.




Test after restoring the internet connection.




Confirm that an error does not permanently disable the Refresh button.

Peer testing questions

Ask a peer tester to consider the following:

•
Is it immediately clear what the application does?

•
Is the city input easy to find and use?

•
Is the weather information readable?

•
Are the error messages understandable?

•
Is the Refresh button clearly labelled?

•
Does the application feel responsive while loading?

•
What visual improvements would make the application easier to use?




Building an Android APK

Flet can package the application as an Android APK. Before building, test the application normally with Python and ensure that all dependencies are listed in requirements.txt.

From the project folder, run:

Plain Text


flet build apk



If the flet command is not recognised, try:

Plain Text


python -m flet build apk



Depending on the Flet version and local development environment, Android build tools may need to be installed or configured. The build process may take several minutes the first time because required Android components may need to be downloaded.

Before distributing the APK, verify that:

•
The app launches on an Android device or emulator.

•
The weather request works on a mobile internet connection.

•
The layout fits a small screen.

•
Text remains readable without horizontal scrolling.

•
The Refresh button is easy to tap.

•
Network errors are displayed correctly.

•
No development-only files or credentials are included.

For current packaging guidance, see the 

Flet publishing documentation.




Troubleshooting

ModuleNotFoundError: No module named 'requests'

Install the Requests package inside the active virtual environment:

Plain Text


python -m pip install requests



ModuleNotFoundError: No module named 'flet'

Install Flet:

Plain Text


python -m pip install flet



Confirm that the virtual environment is active before installing.

AttributeError: module 'flet' has no attribute 'ElevatedButton'

This means the code is using the old Flet button API. Flet 1.0 and later use ft.Button instead of ft.ElevatedButton.

Use:

Python


refresh_button = ft.Button(
    content="Refresh Weather",
    icon=ft.Icons.REFRESH,
    on_click=load_weather,
)



Do not use:

Python


ft.ElevatedButton(text="Refresh Weather")



No such file or directory: weather_app.py

Make sure the terminal is inside the folder containing the Python file:

Plain Text


cd "C:\path\to\Capstone"
python .\weather_app.py



You can list the files in the current folder with:

Plain Text


dir



Confirm that weather_app.py appears in the list.

Could not open requirements file

This means that requirements.txt is not in the current folder. Create the file inside the same folder as weather_app.py, then add:

Plain Text


flet
requests



Run the installation command from that folder:

Plain Text


python -m pip install -r requirements.txt



The application opens but cannot load weather data

Check the following:

1.
Confirm that the device has internet access.

2.
Try searching for a common city such as London or New York.

3.
Check whether Open-Meteo is available.

4.
Try the request again using the Refresh button.

5.
Confirm that the system firewall or network is not blocking Python.

PowerShell prevents virtual environment activation

If PowerShell blocks the activation script, open PowerShell as a user with appropriate permissions or run:

Plain Text


Set-ExecutionPolicy -Scope CurrentUser RemoteSigned



Then activate the environment again:

Plain Text


.\.venv\Scripts\Activate.ps1



Only change the execution policy if it is permitted by your computer's security policy.




Possible Improvements

The current application provides the core functionality required for a live-data dashboard. Future versions could include:

•
Fahrenheit and Celsius unit selection

•
Five-day or seven-day forecasts

•
Automatic location detection

•
Saved favourite cities

•
Recent search history

•
Sunrise and sunset times

•
Weather warnings and alerts

•
A dark-mode theme

•
More detailed weather icons

•
Offline caching of the last successful result

•
A settings screen

•
Accessibility improvements, including larger text options

•
A last-updated timestamp

•
A retry button shown only after a failed request

•
Automated unit and integration tests

•
A CI workflow for linting and testing




Development Notes

When modifying the application:

1.
Keep network requests inside clearly defined functions.

2.
Preserve user-friendly error messages.

3.
Avoid placing API or business logic directly inside visual layout definitions where possible.

4.
Test both successful and failed requests after making changes.

5.
Keep API response parsing defensive because external responses can change or be incomplete.

6.
Update requirements.txt whenever a new dependency is added.

7.
Do not commit the .venv folder to source control.

8.
Keep screenshots and optional assets inside the assets/ folder.

A suitable .gitignore entry for this project is:

Plain Text


.venv/
__pycache__/
*.pyc
.vscode/
.idea/
.DS_Store






Data Source and Attribution

Weather data is provided by 

Open-Meteo.

The user interface is built with 

Flet.

The application uses the Python 

Requests library for HTTP communication.

Review the relevant service terms and attribution requirements before using the application commercially or redistributing it.




License

This project is intended for educational and demonstration purposes as part of a Python and application-development capstone project.

No specific open-source license has been selected for this project. If the project will be distributed publicly, add an appropriate license file, such as the MIT License, and update this section accordingly.




Author

Created as a capstone project for the FNB App Academy Python learning programme.

Replace this section with the author's name, student number, repository link, and contact details if required:

Plain Text


Author: Katlego sambo
Email: Ksambo.dev@gmail.com



