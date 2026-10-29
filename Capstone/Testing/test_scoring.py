from services.scoring import outdoor_score, smart_briefing


def test_rain_lowers_score_and_recommends_umbrella():
    current = {"wind_speed_10m": 10, "weather_code": 63}
    daily = {"precipitation_probability_max": [80], "uv_index_max": [2]}
    assert outdoor_score(current, daily) < 70
    assert smart_briefing(current, daily) == "Carry an umbrella"


def test_clear_conditions_have_positive_briefing():
    current = {"wind_speed_10m": 8, "weather_code": 0}
    daily = {"precipitation_probability_max": [5], "uv_index_max": [3]}
    assert outdoor_score(current, daily) > 70
    assert smart_briefing(current, daily) == "Excellent conditions to explore"
