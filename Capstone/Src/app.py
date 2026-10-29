"""Atmosphere Weather Intelligence - Flask application."""
from flask import Flask, jsonify, render_template, request
from services.weather import WeatherService, WeatherServiceError

app = Flask(__name__)
weather_service = WeatherService()


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/search")
def search():
    query = request.args.get("q", "", type=str).strip()
    if not query:
        return jsonify({"results": [], "error": "Enter a city to search."}), 400
    if len(query) > 100:
        return jsonify({"results": [], "error": "Search query is too long."}), 400
    try:
        return jsonify({"results": weather_service.search_places(query)})
    except WeatherServiceError as exc:
        return jsonify({"error": str(exc), "results": []}), 502


@app.get("/api/weather")
def weather():
    try:
        latitude = float(request.args["lat"])
        longitude = float(request.args["lon"])
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Valid lat and lon query parameters are required."}), 400
    if not (-90 <= latitude <= 90 and -180 <= longitude <= 180):
        return jsonify({"error": "Coordinates are out of range."}), 400
    try:
        return jsonify(weather_service.forecast(latitude, longitude))
    except WeatherServiceError as exc:
        return jsonify({"error": str(exc)}), 502


@app.errorhandler(404)
def not_found(_error):
    return jsonify({"error": "Not found."}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port= int(__import__("os").environ.get("PORT", "5000")), debug=True)
