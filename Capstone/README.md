# Atmosphere Weather Intelligence — Python Capstone

Atmosphere is a Flask weather dashboard that turns live Open-Meteo forecasts into practical outdoor guidance. It includes worldwide city search, current conditions, a 12-hour forecast, a seven-day forecast, favorites, Celsius/Fahrenheit switching, dark/light theme switching, shareable forecast URLs, and weather-based activity advice.

## Run locally

```bash
cd atmosphere-python
python3 -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000.

## Test

```bash
pytest -q
```

## API routes

- `GET /` — dashboard page
- `GET /api/search?q=London` — city search proxy
- `GET /api/weather?lat=-26.2&lon=28.0` — forecast proxy

The backend validates coordinates, handles upstream API errors, and keeps all Open-Meteo requests in `services/weather.py`. The scoring and smart briefing rules are isolated in `services/scoring.py` so they can be tested independently.

Weather and geocoding data are provided by [Open-Meteo](https://open-meteo.com/). No API key is required.
