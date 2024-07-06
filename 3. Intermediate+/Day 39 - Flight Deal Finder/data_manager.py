import requests
from requests.auth import HTTPBasicAuth # Lets do Basic Auth this time for Sheety
import pprint
from API_KEYS import AMADEUS_API_KEY, AMADEUS_API_SECRET, FLIGHT_DEALS_SHEET_AUTH, SHEETY_USERNAME, SHEETY_PASSWORD
from ENDPOINTS import sheets_endpoint


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.username = SHEETY_USERNAME
        self.password = SHEETY_PASSWORD
        self.authorization = HTTPBasicAuth(self.username, self.password) # I set the Sheety for this sheets to use HTTP Basic Auth this time
        self.sheet_data = {}

    def read_sheets(self):
        # Reads the main sheet (prices) of the Flight Deals google sheet
        # and updates DataManager with destination data
        response = requests.get(url=sheets_endpoint, auth=self.authorization)
        data = response.json()

        self.sheet_data = data['prices']
        pprint.pprint(self.sheet_data)
        return self.sheet_data
    
    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def fill_iata_codes(self):
        for row in self.sheet_data:
            # New data to be inserted into sheets
            new_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheets_endpoint}/{row['id']}",
                json=new_data,
                auth=self.authorization
            )
            print(response.text)
