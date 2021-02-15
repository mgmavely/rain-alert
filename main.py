import requests
import os
from twilio.rest import Client

# Environment variables: Twillio
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
TWILIO_PHONE = os.environ.get("TWILIO_PHONE")
PHONE_OUT = os.environ.get("PHONE_OUT")

# Environment variables: OpenWeather
APPID = os.environ.get("APPID")

info = {
    "lat": 43.591290,
    "lon": -79.650253,
    "appid": os.environ.get("APPID"),
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=info)
response.raise_for_status()
weather_data = response.json()
first_twelve = weather_data['hourly'][0:12]

for i in first_twelve:
    condition = i['weather'][0]['id']
    if condition < 700:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        message = client.messages.create(
            body="Bring an umbrella when going out today! ☂️",
            from_=TWILIO_PHONE,
            to=PHONE_OUT
        )

        print(message.status)
        break
