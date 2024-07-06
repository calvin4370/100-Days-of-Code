import requests

# This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from API_KEYS import AMADEUS_API_KEY, AMADEUS_API_SECRET, FLIGHT_DEALS_SHEET_AUTH

# --------------------  -------------------- #

if __name__ == '__main__':
    data_manager = DataManager()
    flight_search = FlightSearch()
    
    sheet_data = data_manager.read_sheets()

    #  5. In main.py check if sheet_data contains any values for the "iataCode" key.
    #  If not, then the IATA Codes column is empty in the Google Sheet.
    #  In this case, pass each city name in sheet_data one-by-one
    #  to the FlightSearch class to get the corresponding IATA code
    #  for that city using the Flight Search API.
    #  You should use the code you get back to update the sheet_data dictionary.
    if sheet_data[0]["iataCode"] == "":
        for row in sheet_data:
            row["iataCode"] = flight_search.get_destination_code(row["city"])

        print(f"sheet_data:\n {sheet_data}")
        data_manager.fill_iata_codes()
