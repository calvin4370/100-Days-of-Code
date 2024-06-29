import requests

url = 'https://opentdb.com/api.php'

parameters = {
    'amount': 10,
    'category': 20,
    'type': 'boolean'
}

response = requests.get(url, params=parameters)
response.raise_for_status()
json_data = response.json()

question_data = json_data['results']