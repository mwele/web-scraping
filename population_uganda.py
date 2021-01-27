import requests
from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup

html_data =urlopen("https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Uganda")
soup=BeautifulSoup(html_data.read(),'lxml')
#print(soup)
cities = soup.find('div', class_='div-col')
cities =cities.get_text()
#for city in cities :
print(cities)