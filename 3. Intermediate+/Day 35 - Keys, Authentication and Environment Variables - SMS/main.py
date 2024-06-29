import requests
import json
import os
import datetime

from twilio.rest import Client

# OpenWeatherMap API
OWM_api_key = os.environ.get("OWM_API_KEY")

# Punggol Coordinates
lat = 1.398490
lon = 103.907921

# Twilio API
# With environment variables
account_sid = os.environ["TWILIO_WHATSAPP_SID"] # For WhatsApp only
auth_token = os.environ["TWILIO_WHATSAPP_AUTH_TOKEN"] # For WhatsApp only
my_phone_number = os.environ["PERSONAL_PHONE_NUMBER"]

# ----------------------------------------------- OpenWeatherMap API call ------------------------------------------------------ #

OWM_endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
params = {
    # Compulsory parameters
    'lat': lat,
    'lon': lon,
    'appid': OWM_api_key,

    # Extra parameters to tailor response
    'cnt': 4, # specify number of timestamps
}
response = requests.get(OWM_endpoint, params=params)

print('Checking weather forecasts for Punggol')
response.raise_for_status()
weather_data = response.json()

three_hourly_blocks = weather_data['list']
names = ['+3 hrs', '+6 hrs', '+9 hrs', '+12 hrs']

# Build message body
datetime_now = datetime.datetime.now()
body = f"""*{datetime_now}*\n\n"""

will_rain = False
for block, name in zip(three_hourly_blocks, names):
    weather_id = block['weather'][0]['id']
    main_weather_type = block['weather'][0]['main']
    description = block['weather'][0]['description']
    
    body += f"""{name}: {description.title()}\n"""

    if weather_id < 700:
        will_rain = True

if will_rain:
    body += f"""\nYou should bring an umbrella if you go outside today ☔"""
else:
    body += f"""\nNo need to bring an umbrella today 🌂"""


# To visualise json
with open('weather_data.json', 'w') as file:
    json.dump(weather_data, file)

# ------------------------------------------------- Use Twilio to send WhatsApp msg to my phone number ---------------------------------------------------- #
print(account_sid, auth_token)
client = Client(account_sid, auth_token)

message = client.messages.create(
    body=body,
    from_="whatsapp:+14155238886",
    to=f'whatsapp:{my_phone_number}',
)

print(message.body)
print(message.status)