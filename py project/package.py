#https://mail.google.com/mail/u/0/#inbox
#dire le titre de cette page
#afficher la classe "gb_Ca gbii"

import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
link = requests.get(url)
page = link.content
soup = BeautifulSoup(page, "html.parser")
descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")

print(soup.title.string)
print(descriptions)