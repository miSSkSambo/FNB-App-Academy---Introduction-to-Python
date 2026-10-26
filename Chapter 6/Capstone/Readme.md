Live Weather Dashboard

A simple weather dashboard built with Python, Flet, and the free Open-Meteo API. The app allows users to search for a city and view its current temperature, weather conditions, humidity, apparent temperature, and wind speed.

Features

•
Search for weather by city name

•
Convert city names into geographic coordinates using Open-Meteo geocoding

•
Display current weather information

•
Show temperature in degrees Celsius

•
Display weather conditions with icons

•
Show apparent temperature, humidity, and wind speed

•
Refresh weather data with a button

•
Display a loading indicator while data is being retrieved

•
Handle network errors and invalid city names with user-friendly messages

•
No API key required

Technologies Used

•
Python 3

•
Flet

•
Requests

•
Open-Meteo Geocoding API

•
Open-Meteo Forecast API

Project Structure

Plain Text


weather-dashboard/
├── weather_app.py       # Main Flet application
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation



Requirements

Make sure Python 3.9 or later is installed on your computer.

You also need an active internet connection because the app retrieves live data from Open-Meteo.

Installation

1. Clone or download the project

Download the project files or clone the repository:

Bash


git clone https://github.com/your-username/weather-dashboard.git
cd weather-dashboard



Replace the repository URL with the correct project URL if the project is hosted on GitHub.

2. Create a virtual environment

Creating a virtual environment is recommended so that the project dependencies remain separate from other Python projects.

Windows

Bash


python -m venv .venv
.venv\Scripts\activate



macOS or Linux

Bash


python3 -m venv .venv
source .venv/bin/activate



3. Install the dependencies

Bash


pip install -r requirements.txt



If a requirements.txt file is not available, install the packages directly:

Bash


pip install flet requests



Running the Application

Start the application with:

Bash


python weather_app.py



On macOS or Linux, you may need to use:

Bash


python3 weather_app.py



The application opens a Flet window and loads the weather for London by default.

How to Use the App

1.
Enter the name of a city in the search field.

2.
Click Refresh Weather.

3.
Wait for the app to retrieve the latest weather data.

4.
View the city name, temperature, weather condition, humidity, apparent temperature, and wind speed.

5.
If the city cannot be found or the network request fails, read the error message shown below the weather card.

API Information

This application uses Open-Meteo, a free weather service that does not require an API key.

Geocoding endpoint

The geocoding endpoint converts a city name into latitude and longitude coordinates:

Plain Text


https://geocoding-api.open-meteo.com/v1/search



Weather endpoint

The weather endpoint uses the coordinates to retrieve current weather information:

Plain Text


https://api.open-meteo.com/v1/forecast



The application requests the following current weather values:

•
Temperature

•
Relative humidity

•
Apparent temperature

•
Weather code

•
Wind speed

More information is available in the 

Open-Meteo documentation.

Error Handling

The application handles several common problems:

•
Empty city name

•
City not found

•
Slow network requests

•
No internet connection

•
HTTP errors from the API

•
Unexpected or incomplete API responses

Example error messages include:

Plain Text


Please enter a city name.



Plain Text


Unable to connect to the weather service. Please check your internet connection.



Plain Text


The request took too long. Please check your connection and try again.



Testing Checklist

Use the following checklist to test the application:




The app starts successfully.




Weather for the default city loads on startup.




A valid city returns weather information.




An empty search field displays an error message.




An unknown city displays a suitable error message.




The Refresh button retrieves updated data.




A disconnected network displays a user-friendly error.




The loading indicator appears while data is being requested.




Temperature, humidity, apparent temperature, and wind speed are displayed correctly.




The layout remains readable when the window is resized.

Building an APK

Flet can be used to package the application for Android. Install the Flet command-line tools if necessary, then use the following command from the project directory:

Bash


flet build apk



Depending on the installed Flet version and operating system, additional Android or Java development tools may be required. Consult the 

Flet packaging documentation if the build command reports a missing dependency.

Before building the APK, check that:

•
The app runs correctly with python weather_app.py.

•
All dependencies are listed in requirements.txt.

•
No test credentials or unnecessary files are included.

•
The application has been tested on a mobile-sized screen.

•
The project has a clear name and icon if required.

Dependencies

The project requires:

Plain Text


flet
requests



These dependencies should be listed in requirements.txt:

Plain Text


flet
requests



Possible Improvements

Future versions could include:

•
Temperature unit selection between Celsius and Fahrenheit

•
A five-day forecast

•
Automatic location detection

•
Saved favourite cities

•
Weather alerts

•
Sunrise and sunset times

•
A dark mode

•
More detailed weather icons

•
Offline caching of the most recent weather result

Credits and Attribution

Weather data is provided by 

Open-Meteo.

The application interface is built with 

Flet.

License

This project is intended for educational and demonstration purposes. Add an appropriate license, such as the MIT License, before distributing the project publicly.

