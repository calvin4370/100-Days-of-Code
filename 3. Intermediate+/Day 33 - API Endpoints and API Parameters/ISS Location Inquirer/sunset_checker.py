import requests
import datetime

url = 'https://api.sunrise-sunset.org/json'

punggol_lat = 1.398490
punngol_long = 103.907921

# The sunrise sunset api requires you to first porvide it with a set of coodinates formatted as such before they will return the data you want
parameters = {
    'lat': punggol_lat,
    'lng': punngol_long,
    'formatted': 0
}

# The api wants a set of specific parameters, input them as such
response = requests.get(url, params=parameters)
response.raise_for_status()

json_data = response.json()

# print(json_data)
"""
{'results': {'sunrise': '2023-12-26T23:02:44+00:00', 
             'sunset': '2023-12-27T11:07:32+00:00', 
             'solar_noon': '2023-12-27T05:05:08+00:00', 
             'day_length': 43488, 
             'civil_twilight_begin': '2023-12-26T22:41:24+00:00', 
             'civil_twilight_end': '2023-12-27T11:28:51+00:00', 
             'nautical_twilight_begin': '2023-12-26T22:15:15+00:00', 
             'nautical_twilight_end': '2023-12-27T11:55:01+00:00', 
             'astronomical_twilight_begin': '2023-12-26T21:49:00+00:00', 
             'astronomical_twilight_end': '2023-12-27T12:21:16+00:00'}, 
             'status': 'OK', 'tzId': 'UTC'}
"""

# Get the hour of the sunrise and sunset times in Punggol, Singapore in UTC time
sunrise_utc = json_data['results']['sunrise'].split('T')[1].split(':')[0]
sunset_utc = json_data['results']['sunset'].split('T')[1].split(':')[0]

# Get the hour of the sunrise and sunset times in Punggol, Singapore in SGT time
sunrise_sgt = (int(sunrise_utc) + 8) % 24
sunset_sgt = (int(sunset_utc) + 8) % 24

# print(sunrise_sgt)
# 7
# print(sunset_sgt)
# 19

hour_now = datetime.datetime.now().hour

if hour_now > sunset_sgt or hour_now < sunrise_sgt:
    sunset = True
    sunrise = False
else:
    sunset = False
    sunrise = True