import requests
from sunset_checker import sunrise, sunset


url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)
response.raise_for_status()

json_data = response.json()

longitude = json_data['iss_position']['longitude']
latitude = json_data['iss_position']['latitude']

iss_position = (longitude, latitude)
print(f"The ISS is at {iss_position}")
