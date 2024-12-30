from bs4 import BeautifulSoup as BS
import requests

date = input('Which date do you want to travel to? (YYYY-MM-DD): ')

# Get a response from url
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url=url, headers=headers)

# Make the soup
soup = BS(response.text, 'lxml')
song_name_spans = soup.select("li ul li h3") # select all h3 within a li ul li h3 chain
song_names = [song.getText().strip() for song in song_name_spans]

