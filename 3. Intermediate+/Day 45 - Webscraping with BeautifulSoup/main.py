'''
Retrieve the html code from a html file
'''

from bs4 import BeautifulSoup
import requests
import lxml

with open('website.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'lxml')
# print(soup)
# <!DOCTYPE html>
# <html>
# <head>
# <meta charset="utf-8"/>
# <title>Angela's Personal Site</title>
# </head>
# <body>
# <h1 id="name">Angela Yu</h1>
# <p><em>Founder of <strong><a href="https://www.appbrewery.co/">The App Brewery</a></strong>.</em></p>
# <p>I am an iOS and Web Developer. I luv coffee and motorcycles.</p>
# <hr/>
# <h3 class="heading">Books and Teaching</h3>
# <ul>
# <li>The Complete iOS App Development Bootcamp</li>
# <li>The Complete Web Development Bootcamp</li>
# <li>100 Days of Code - The Complete Python Bootcamp</li>
# </ul>
# <hr/>
# <h3 class="heading">Other Pages</h3>
# <a href="https://angelabauer.github.io/cv/hobbies.html">My Hobbies</a>
# <a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>
# </body>
# </html>

# -------------------- Find the first of each tag -------------------- #

print(soup.title)
# <title>Angela's Personal Site</title>

print(soup.title.name)
# title

print(soup.title.string)
# Angela's Personal Site

print(soup.a) # returns the first anchor tag that exists
# <a href="https://www.appbrewery.co/">The App Brewery</a>

print(soup.find('a')) # Same thing ^
# <a href="https://www.appbrewery.co/">The App Brewery</a>

print(soup.button) # returns the first anchor tag that exists
# None


# -------------------- Find all tags of a certain name -------------------- #

all_archor_tags = soup.find_all('a') # by name (first attribute of find_all method)
print(all_archor_tags)
# [<a href="https://www.appbrewery.co/">The App Brewery</a>, 
#  <a href="https://angelabauer.github.io/cv/hobbies.html">My Hobbies</a>, 
#  <a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>]

for a in all_archor_tags:
    print(a.text) # .getText() method does the same thing
# The App Brewery
# My Hobbies
# Contact Me

for a in all_archor_tags:
    print(a.get('href'))
# https://www.appbrewery.co/
# https://angelabauer.github.io/cv/hobbies.html
# https://angelabauer.github.io/cv/contact-me.html


specific_h1 = soup.find_all(name='h1', id='name') # gets a list of tags with specific filters, or you can use find to get just one and not a list
print(specific_h1)
# [<h1 id="name">Angela Yu</h1>]

tags_of_specific_class = soup.find_all(class_='heading')
print(tags_of_specific_class)
# [<h3 class="heading">Books and Teaching</h3>, 
#  <h3 class="heading">Other Pages</h3>]

company_url = soup.select(selector='p a') # Use CSS Selection to find all a tags inside p tags
print(company_url)
# [<a href="https://www.appbrewery.co/">The App Brewery</a>]