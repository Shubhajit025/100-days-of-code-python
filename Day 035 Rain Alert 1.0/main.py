import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

OWM_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = os.getenv("LATITUDE")
MY_LONG = os.getenv("LONGITUDE")
API_KEY = os.getenv("OWM_API_KEY")
ACCOUNT_SID = os.getenv("OWM_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
SEND_TO_PHONE_NUMBER = os.getenv("SEND_TO_PHONE_NUMBER")

parameter = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(url=OWM_API_ENDPOINT, params=parameter)
response.raise_for_status()
# stat_code = response.status_code
weather_data = response.json()

weather_forecast_list = weather_data["list"]

will_rain = False

for hour_data in weather_forecast_list:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        to=SEND_TO_PHONE_NUMBER,
        from_=TWILIO_PHONE_NUMBER,
        body="It's going to rain today. Remember to bring an Umbrella ☔!"
    )
    print(message.status)
