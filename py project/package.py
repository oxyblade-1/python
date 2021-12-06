import requests

from bs4 import BeautifulSoup

url = "https://github.com/oxyblade-1"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')