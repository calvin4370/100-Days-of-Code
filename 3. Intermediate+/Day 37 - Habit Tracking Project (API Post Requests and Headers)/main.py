import requests
from datetime import datetime
from pixela_user_info import TOKEN, USERNAME, VAL_GRAPH_ID

'''
Pixela Starting Out Guide
Step 1: Create your user account
'''
pixela_endpoint = 'https://pixe.la/v1/users'

# POST request to create a user
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


'''
Step 2: Create a graph definition
'''
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_params = {
    'id': VAL_GRAPH_ID,
    'name': 'Valorant Games Played',
    'unit': 'games',
    'type': 'int',
    'color': 'momiji',
}
http_header = {
    'X-USER-TOKEN': TOKEN
} # Put your key in http header instead of body to be more secure

# response = requests.post(url=graph_endpoint, json=graph_params, headers=http_header)
# print(response.text)

'''
Step 3: Get the graph!
Browse https://pixe.la/v1/users/a-know/graphs/test-graph ! This is also /v1/users/<username>/graphs/<graphID> API.
'''

'''
Step 4: Post value to the graph
'''
val_graph_endpoint = f'{graph_endpoint}/{VAL_GRAPH_ID}'

tdy_datetime = datetime.now()
tdy_date = tdy_datetime.strftime('%Y%m%d')
print(tdy_date)

val_post_params = {
    'date': tdy_date, # yyyyMMdd format
    'quantity': '6',
}
# response = requests.post(url=val_graph_endpoint, json=val_post_params, headers={'X-USER-TOKEN': TOKEN})
# print(response.text)