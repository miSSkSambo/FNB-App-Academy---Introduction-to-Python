"""Open-Meteo client used by the Flask API."""
from typing import Any
import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"


class WeatherServiceError(RuntimeError):
    """Raised when Open-Meteo cannot provide a valid response."""


class WeatherService:
    def __init__(self, session: requests.Session | None = None, timeout: int = 10):
        self.session = session or requests.Session()
        self.timeout = timeout

    def _get(self, url: str, params: dict[str, Any]) -> dict[str, Any]:
        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
        except (requests.RequestException, ValueError) as exc:
            raise WeatherServiceError("The forecast service is unavailable right now.") from exc
        if not isinstance(data, dict):
            raise WeatherServiceError("The forecast service returned an invalid response.")
        return data

    def search_places(self, query: str) -> list[dict[str, Any]]:
        data = self._get(GEOCODING_URL, {
            "name": query, "count": 5, "language": "en", "format": "json"
        })
        return data.get("results", [])

    def forecast(self, latitude: float, longitude: float) -> dict[str, Any]:
        return self._get(FORECAST_URL, {
            "latitude": latitude,
            "longitude": longitude,
            "current": ",".join([
                "temperature_2m", "relative_humidity_2m", "apparent_temperature",
                "is_day", "precipitation", "weather_code", "wind_speed_10m",
                "pressure_msl", "uv_index", "visibility",
            ]),
            "hourly": ",".join([
                "temperature_2m", "precipitation_probability", "weather_code",
                "wind_speed_10m", "relative_humidity_2m",
            ]),
            "daily": ",".join([
                "weather_code", "temperature_2m_max", "temperature_2m_min", "sunrise",
                "sunset", "uv_index_max", "precipitation_probability_max",
                "wind_speed_10m_max",
            ]),
            "timezone": "auto",
            "forecast_days": 7,
        })
