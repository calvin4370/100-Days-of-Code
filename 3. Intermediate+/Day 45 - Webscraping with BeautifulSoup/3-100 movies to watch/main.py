import requests
from bs4 import BeautifulSoup as BS

URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BS(website_html, 'lxml')

movies = soup.find_all(name='h3', class_='title')

movie_titles = [movie.getText() for movie in movies]
movies = movie_titles[::-1] # flip order

with open('movies.txt', 'w') as file:
    for movie in movies:
        file.write(f'{movie}\n')
