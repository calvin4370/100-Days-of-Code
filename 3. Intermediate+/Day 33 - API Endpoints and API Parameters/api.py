import requests

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)
response.raise_for_status()

# print(response)
# <Response [200]>

# print(response.status_code)
# 200

# Return the json-encoded content of the response, if any, since we know the api returns json formatted data
json_data = response.json()

# print(json_data)
""" on 27/12/2023 3.00pm
{'message': 'success', 
 'people': [{'name': 'Jasmin Moghbeli', 'craft': 'ISS'}, 
            {'name': 'Andreas Mogensen', 'craft': 'ISS'}, 
            {'name': 'Satoshi Furukawa', 'craft': 'ISS'}, 
            {'name': 'Konstantin Borisov', 'craft': 'ISS'}, 
            {'name': 'Oleg Kononenko', 'craft': 'ISS'}, 
            {'name': 'Nikolai Chub', 'craft': 'ISS'}, 
            {'name': "Loral O'Hara", 'craft': 'ISS'}], 
 'number': 7}
 """

print(f"There is currently {json_data['number']} people in space")
print("They are:")
for person in json_data['people']:
    print(f" - {person['name']}, on the {person['craft']}")