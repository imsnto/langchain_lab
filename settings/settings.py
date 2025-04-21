import  os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

weather_api_key = os.getenv("WEATHER_API_KEY")
grok_api_key = os.getenv("GROK_API_KEY")
weather_url = "http://api.openweathermap.org/data/2.5/weather"