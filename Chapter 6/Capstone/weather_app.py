import requests
import flet as ft


# Open-Meteo weather-code descriptions
WEATHER_CODES = {
    0: ("Clear sky", "☀️"),
    1: ("Mainly clear", "🌤️"),
    2: ("Partly cloudy", "⛅"),
    3: ("Overcast", "☁️"),
    45: ("Fog", "🌫️"),
    48: ("Depositing rime fog", "🌫️"),
    51: ("Light drizzle", "🌦️"),
    53: ("Moderate drizzle", "🌦️"),
    55: ("Dense drizzle", "🌧️"),
    56: ("Light freezing drizzle", "🌧️"),
    57: ("Dense freezing drizzle", "🌧️"),
    61: ("Slight rain", "🌦️"),
    63: ("Moderate rain", "🌧️"),
    65: ("Heavy rain", "🌧️"),
    66: ("Light freezing rain", "🌧️"),
    67: ("Heavy freezing rain", "🌧️"),
    71: ("Slight snow fall", "🌨️"),
    73: ("Moderate snow fall", "❄️"),
    75: ("Heavy snow fall", "❄️"),
    77: ("Snow grains", "❄️"),
    80: ("Slight rain showers", "🌦️"),
    81: ("Moderate rain showers", "🌧️"),
    82: ("Violent rain showers", "⛈️"),
    85: ("Slight snow showers", "🌨️"),
    86: ("Heavy snow showers", "❄️"),
    95: ("Thunderstorm", "⛈️"),
    96: ("Thunderstorm with slight hail", "⛈️"),
    99: ("Thunderstorm with heavy hail", "⛈️"),
}


def main(page: ft.Page):
    page.title = "Live Weather Dashboard"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 25
    page.bgcolor = "#F3F6FA"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    city_input = ft.TextField(
        label="Enter a city",
        hint_text="For example: London",
        value="London",
        width=350,
        prefix_icon=ft.Icons.LOCATION_CITY,
    )

    city_text = ft.Text(
        "Weather Dashboard",
        size=28,
        weight=ft.FontWeight.BOLD,
        color="#16324F",
    )

    location_text = ft.Text(
        "",
        size=18,
        weight=ft.FontWeight.BOLD,
        color="#34526F",
    )

    temperature_text = ft.Text(
        "--°C",
        size=52,
        weight=ft.FontWeight.BOLD,
        color="#16324F",
    )

    condition_text = ft.Text(
        "Enter a city to view the weather",
        size=20,
        color="#34526F",
    )

    details_text = ft.Text(
        "",
        size=14,
        color="#5C6B73",
    )

    status_text = ft.Text(
        "",
        size=14,
        color="#B3261E",
    )

    weather_icon = ft.Text(
        "🌍",
        size=60,
    )

    loading_indicator = ft.ProgressRing(
        width=25,
        height=25,
        visible=False,
    )

    def show_error(message):
        status_text.value = message
        status_text.color = "#B3261E"
        loading_indicator.visible = False
        page.update()

    def load_weather(e=None):
        city = city_input.value.strip()

        if not city:
            show_error("Please enter a city name.")
            return

        loading_indicator.visible = True
        status_text.value = "Loading weather data..."
        status_text.color = "#34526F"
        page.update()

        try:
            # First, convert the city name into latitude and longitude
            geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"

            geocoding_response = requests.get(
                geocoding_url,
                params={
                    "name": city,
                    "count": 1,
                    "language": "en",
                    "format": "json",
                },
                timeout=10,
            )

            geocoding_response.raise_for_status()
            location_data = geocoding_response.json()

            if not location_data.get("results"):
                show_error(f"Could not find a location called '{city}'.")
                return

            location = location_data["results"][0]

            latitude = location["latitude"]
            longitude = location["longitude"]
            found_city = location.get("name", city)
            country = location.get("country", "")

            # Request the current weather
            weather_url = "https://api.open-meteo.com/v1/forecast"

            weather_response = requests.get(
                weather_url,
                params={
                    "latitude": latitude,
                    "longitude": longitude,
                    "current": (
                        "temperature_2m,"
                        "relative_humidity_2m,"
                        "apparent_temperature,"
                        "weather_code,"
                        "wind_speed_10m"
                    ),
                    "temperature_unit": "celsius",
                    "wind_speed_unit": "kmh",
                    "timezone": "auto",
                },
                timeout=10,
            )

            weather_response.raise_for_status()
            weather_data = weather_response.json()

            current_weather = weather_data["current"]

            temperature = current_weather["temperature_2m"]
            feels_like = current_weather["apparent_temperature"]
            humidity = current_weather["relative_humidity_2m"]
            wind_speed = current_weather["wind_speed_10m"]
            weather_code = current_weather["weather_code"]

            condition, icon = WEATHER_CODES.get(
                weather_code,
                ("Unknown conditions", "🌍"),
            )

            city_text.value = "Live Weather Dashboard"
            location_text.value = f"{found_city}, {country}"
            weather_icon.value = icon
            temperature_text.value = f"{temperature:.1f}°C"
            condition_text.value = condition

            details_text.value = (
                f"Feels like: {feels_like:.1f}°C    "
                f"Humidity: {humidity}%    "
                f"Wind: {wind_speed:.1f} km/h"
            )

            status_text.value = "Weather data updated successfully."
            status_text.color = "#26734D"
            loading_indicator.visible = False
            page.update()

        except requests.exceptions.Timeout:
            show_error(
                "The request took too long. Please check your connection and try again."
            )

        except requests.exceptions.ConnectionError:
            show_error(
                "Unable to connect to the weather service. "
                "Please check your internet connection."
            )

        except requests.exceptions.HTTPError:
            show_error(
                "The weather service returned an error. Please try again later."
            )

        except (KeyError, ValueError):
            show_error(
                "The weather data was not in the expected format."
            )

        except Exception as error:
            print(f"Unexpected error: {error}")
            show_error(
                "Something went wrong. Please try again."
            )

    refresh_button = ft.ElevatedButton(
        text="Refresh Weather",
        icon=ft.Icons.REFRESH,
        on_click=load_weather,
        style=ft.ButtonStyle(
            bgcolor="#1976D2",
            color="#FFFFFF",
            padding=15,
        ),
    )

    weather_card = ft.Card(
        elevation=5,
        content=ft.Container(
            content=ft.Column(
                controls=[
                    location_text,
                    ft.Row(
                        controls=[
                            weather_icon,
                            temperature_text,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    condition_text,
                    ft.Divider(),
                    details_text,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=12,
            ),
            padding=25,
            width=500,
            bgcolor="#FFFFFF",
            border_radius=15,
        ),
    )

    page.add(
        ft.Column(
            controls=[
                city_text,
                ft.Text(
                    "Get current weather conditions for any city",
                    size=15,
                    color="#5C6B73",
                ),
                ft.Row(
                    controls=[
                        city_input,
                        refresh_button,
                        loading_indicator,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    wrap=True,
                ),
                weather_card,
                status_text,
                ft.Text(
                    "Data provided by Open-Meteo",
                    size=12,
                    color="#7A8A99",
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=18,
        )
    )

    # Load the default city's weather when the app starts
    load_weather()


if __name__ == "__main__":
    ft.run(main)
