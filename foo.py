import requests
from bs4 import BeautifulSoup

foo=requests.get("https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Uganda").text
soup=BeautifulSoup(foo,'lxml')
print(soup)