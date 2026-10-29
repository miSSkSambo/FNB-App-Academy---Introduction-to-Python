"""Pure functions for Atmosphere's practical weather guidance."""


def outdoor_score(current: dict, daily: dict) -> int:
    rain = float((daily.get("precipitation_probability_max") or [0])[0] or 0)
    uv = float((daily.get("uv_index_max") or [0])[0] or 0)
    wind = float(current.get("wind_speed_10m") or 0)
    return max(8, min(98, round(100 - rain * 0.45 - wind * 0.7 - uv * 1.5)))


def smart_briefing(current: dict, daily: dict) -> str:
    rain = float((daily.get("precipitation_probability_max") or [0])[0] or 0)
    uv = float((daily.get("uv_index_max") or [0])[0] or 0)
    wind = float(current.get("wind_speed_10m") or 0)
    code = int(current.get("weather_code") or 0)
    if rain >= 55 or code >= 61:
        return "Carry an umbrella"
    if uv >= 7:
        return "Sun protection recommended"
    if wind >= 35:
        return "Secure loose outdoor items"
    return "Excellent conditions to explore"
