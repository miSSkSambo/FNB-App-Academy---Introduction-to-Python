from unittest.mock import Mock
from app import app, weather_service


def test_home_page_loads():
    app.config["TESTING"] = True
    assert app.test_client().get("/").status_code == 200


def test_weather_requires_coordinates():
    app.config["TESTING"] = True
    response = app.test_client().get("/api/weather")
    assert response.status_code == 400


def test_search_uses_service(monkeypatch):
    app.config["TESTING"] = True
    monkeypatch.setattr(weather_service, "search_places", lambda query: [{"name": query}])
    response = app.test_client().get("/api/search?q=London")
    assert response.status_code == 200
    assert response.get_json()["results"] == [{"name": "London"}]
