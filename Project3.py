__author__ = 'Jessy'


from bs4 import BeautifulSoup

import requests


url = "http://www.abcnews.com/los-angeles-CA/news?g=los%20angels%2C%ca&q=news"

r = requests.get(url)

data = r.text

soup = BeautifulSoup(r.content)

for link in soup.find_all('a'):
    print(link.get('href'))


