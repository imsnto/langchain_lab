import requests
from settings.settings import  weather_api_key, weather_url

def calculator(expression):
    """Evaluate a basic arithmetic expression (e.g. '5 + 3', '10 * 2')."""
    try:
        result = eval(expression, {"__builtins__": {}})
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {e}"

def get_weather(location):
    """Get the current/real-time weather for a given location."""
    try:
        params = {
            'appid': weather_api_key,
            'q': location,
            'units': 'metric', # Use 'imperial' for Farhenheit
        }
        response =  requests.get(weather_url, params=params)
        if response.status_code == 200:
            data =  response.json()
            weather = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']

            return f"Weather in {location}: {weather}, Temperature: {temperature}°C, Humidity: {humidity}%"
        else:
            return f"Error fetching weather data: {response.status_code}"
    except Exception as e:
        return f"Error fetching weather data: {e}"
