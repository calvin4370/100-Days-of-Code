from bs4 import BeautifulSoup
import requests

# Getting html code from a live website
response = requests.get('https://news.ycombinator.com/news')
html_content = response.text

soup = BeautifulSoup(html_content, 'lxml')

# -------------------- Webscraping the live site -------------------- #

title_line_spans = soup.find_all(class_='titleline')
for counter, span in enumerate(title_line_spans):
    anchor = span.a
    upvotes = span
    print(counter + 1, anchor.text)