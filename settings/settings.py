import  os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

weather_api_key = os.getenv("WEATHER_API_KEY")
grok_api_key = os.getenv("GROQ_API_KEY")
weather_url = "http://api.openweathermap.org/data/2.5/weather"

class Settings:
    weather_api_url = "http://api.openweathermap.org/data/2.5/weather"
    weather_api_key = os.getenv("WEATHER_API_KEY")
    groq_api_key = os.getenv("GROQ_API_KEY")

settings = Settings()