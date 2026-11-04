
# Atmosphere --- Weather Intelligence

**Read the sky before it happens.**

A responsive weather dashboard that turns live forecasts into practical,
shareable guidance for wherever you are going next.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20App-000000?logo=flask&logoColor=white)
![Weather
Data](https://img.shields.io/badge/Weather%20Data-Open--Meteo-38BDF8)
![Tests](https://img.shields.io/badge/Tests-pytest-0A9EDC?logo=pytest&logoColor=white)
![API Key](https://img.shields.io/badge/API%20Key-Not%20Required-2EA44F)
![Status](https://img.shields.io/badge/Project-Python%20Capstone-7C3AED)
:::

------------------------------------------------------------------------

## Overview

Atmosphere is a Flask-powered weather dashboard designed to make
forecast information easier to understand and act on. It retrieves
weather and geocoding data from [Open-Meteo](https://open-meteo.com/)
and presents it through a clean, responsive interface with practical
outdoor guidance.

Search for cities around the world, review current conditions and
upcoming forecasts, save favourite locations, and share a forecast with
a direct URL.

## Features

-   **Worldwide city search** --- find locations by city name.
-   **Current weather conditions** --- view the latest available
    conditions for a selected location.
-   **12-hour forecast** --- review conditions throughout the day.
-   **Seven-day forecast** --- plan ahead with a week-long outlook.
-   **Activity guidance** --- get weather-based suggestions for outdoor
    activities.
-   **Favourite locations** --- save places you want to check again.
-   **Temperature units** --- switch between Celsius and Fahrenheit.
-   **Appearance controls** --- switch between dark and light themes.
-   **Shareable forecast links** --- share a location's forecast using
    its URL.
-   **Backend validation and error handling** --- validate coordinates
    and handle upstream API errors.

## Preview

Run the application locally to explore the dashboard.

``` text
http://127.0.0.1:5000
```

## Tech stack

  Area                         Technology
  ---------------------------- -----------------------
  Backend                      Python, Flask
  Frontend                     HTML, CSS, JavaScript
  Weather and geocoding data   Open-Meteo
  Automated tests              pytest

## Getting started

### Requirements

-   Python 3.10 or newer
-   pip
-   Git (optional, if cloning the repository)

No Open-Meteo API key is required.

### 1. Get the project

If you already have the project ZIP, extract it and open the
`atmosphere-python` folder in Visual Studio Code.

Alternatively, clone the repository:

``` bash
git clone <repository-url>
cd atmosphere-python
```

Replace `<repository-url>` with the actual Git repository URL.

### 2. Create a virtual environment

**Windows --- PowerShell**

``` powershell
py -m venv .venv
```

**macOS / Linux**

``` bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

**Windows --- PowerShell**

``` powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks script activation, run this for the current
terminal session and activate again:

``` powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

**Windows --- Command Prompt**

``` bat
.venv\Scripts\activate.bat
```

**macOS / Linux**

``` bash
source .venv/bin/activate
```

### 4. Install dependencies

``` bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Start the application

``` bash
python app.py
```

When Flask starts successfully, open:

**http://127.0.0.1:5000**

To stop the development server, press `Ctrl + C` in the terminal.

> **Note:** Flask's built-in server is intended for local development.
> Use a production WSGI server when deploying the application.

## Running the tests

With the virtual environment activated, run:

``` bash
pytest -q
```

The test suite is located in the `tests/` directory.

## API routes

The Flask application exposes the following routes:

  -----------------------------------------------------------------------------------
  Method                  Endpoint                            Purpose
  ----------------------- ----------------------------------- -----------------------
  `GET`                   `/`                                 Serves the weather
                                                              dashboard.

  `GET`                   `/api/search?q=London`              Searches for a city
                                                              through the backend.

  `GET`                   `/api/weather?lat=-26.2&lon=28.0`   Retrieves forecast data
                                                              for the supplied
                                                              coordinates.
  -----------------------------------------------------------------------------------

The backend keeps Open-Meteo requests in `services/weather.py`. Weather
scoring and smart briefing rules are separated into
`services/scoring.py` so they can be tested independently.

## Project structure

``` text
atmosphere-python/
├── services/
│   ├── scoring.py
│   └── weather.py
├── static/
│   ├── app.js
│   ├── favicon.svg
│   └── styles.css
├── templates/
│   └── index.html
├── tests/
│   ├── test_app.py
│   └── test_scoring.py
├── app.py
├── requirements.txt
└── README.md
```

## Data provider

Weather forecasts and geocoding data are provided by
[Open-Meteo](https://open-meteo.com/). The application does not require
an API key for the configured Open-Meteo services.

## Troubleshooting

**`ModuleNotFoundError` when starting the app**

Activate the project's virtual environment and install the dependencies:

``` bash
python -m pip install -r requirements.txt
```

**The `python` command is not recognised on Windows**

Try using the Python launcher:

``` powershell
py -m venv .venv
py -m pip install -r requirements.txt
py app.py
```

**The page does not load**

-   Confirm that `python app.py` is still running.
-   Check the terminal for error messages.
-   Open `http://127.0.0.1:5000` in your browser.
-   If port `5000` is already in use, stop the other process using it
    before restarting Atmosphere.

**City search or weather data does not load**

Check your internet connection and review the terminal output for
upstream service or network errors.

## Contributing

Contributions and improvements are welcome.

1.  Create a branch for your change.
2.  Make your updates.
3.  Run the tests with `pytest -q`.
4.  Submit a pull request describing the change.

## Acknowledgements

-   [Open-Meteo](https://open-meteo.com/) for weather forecast and
    geocoding data.
-   [Flask](https://flask.palletsprojects.com/) for the Python web
    framework.
-   [pytest](https://docs.pytest.org/) for the testing framework.

------------------------------------------------------------------------


**Atmosphere --- Weather, decoded.**

Built as a Python capstone project.
:::
