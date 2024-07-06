'''
Create an app that takes plain text as input and uses a natural language model to parse the input to understand what workouts you have completed
and writes info into a Google Sheets
'''

import os
import requests
import datetime

# Nutritionix API inputs
nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
APP_ID = 'b230d5ab'
API_KEY = os.environ.get('NUTRITIONIX_API_KEY', 'Environment Variable "NUTRITIONIX_API_KEY" missing')

# Example Health Information
gender = 'male'
weight_kg = 58
height_cm = 179
age = 21

# Google Sheets Info
# Sheety API
workout_tracking_sheets = 'https://docs.google.com/spreadsheets/d/1krTF8KUL_kbEoEOix87J6gWd8s3j3CyGST7xWCboCI4/edit?gid=0#gid=0'
sheet_endpoint = 'https://api.sheety.co/cd273041e691a6f4c49f23929277e083/myWorkouts (day38Of100DaysOfCode)/workouts' # To edit 'My Workouts' sheets through Sheety API

def query_nutritionix():
    '''
    Simply queries Nutritionix and uses their NLM to determine what exercises you did based on the plain text inputted
    '''
    query = input("Tell me which exercises you did: ")
    nutritionix_params = {
        'query': query,
        'gender': gender,
        'weight_kg': weight_kg,
        'height_cm': height_cm,
        'age': age,
    }
    response = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers={'x-app-id': APP_ID, 'x-app-key': API_KEY})
    result = response.json()
    print(result)

def update_sheets():
    '''
    Adds rows to the Google Sheets after querying Nutritionix and using their NLM to determine what exercises you did based on the plain text inputted
    '''
    exercise_text = input("Tell me which exercises you did: ")
    nutritionix_params = {
        'query': exercise_text,
        'gender': gender,
        'weight_kg': weight_kg,
        'height_cm': height_cm,
        'age': age,
    }
    response = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers={'x-app-id': APP_ID, 'x-app-key': API_KEY})
    exercises = response.json()['exercises']
    import json
    with open('data.json', 'w') as file:
        json.dump(exercises, file)
    curr_datetime = datetime.datetime.now()

    curr_date = curr_datetime.strftime('%d/%m/%Y')
    curr_time = curr_datetime.strftime('%I:%M%p').lower()

    # Exercise information
    for exercise_event in exercises:
        name = exercise_event['name'].title()
        duration = exercise_event['duration_min']
        calories = exercise_event['nf_calories']
        add_row(curr_date, curr_time, name, duration, calories)

    if not exercises:
        print('No exercises input')

def add_row(date, time, exercise, duration, calories):
    '''
    Adds a row to the Workout Tracking Google Sheets
    '''
    sheet_inputs = { # By worksheet, parameter names
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }
    # I set my sheety API to require an auth key to edit this specific sheets, I set it to the same as my Nutritionix API key, but the format is as so:
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers={'Authorization': f'Bearer {API_KEY}'})
    print(sheet_response.text) # For debug in console

def format_time(mins):
    '''
    formats mins (str) into h, mins (str) if possible
    '''
    mins = int(mins)
    h = mins // 60
    mins = mins % 60

    if not h:
        return f'{mins}min'
    elif h and not min:
        return f'{h}h'
    else:
        return f'{h}h {mins}min'

update_sheets()
