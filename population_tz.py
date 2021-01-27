from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
html_data=urlopen("https://en.wikipedia.org/wiki/List_of_cities_in_Tanzania")
soup=BeautifulSoup(html_data.read(),'lxml')
cities=soup.find('tbody')
cities=cities.get_text()
#for city in cities:
#city_name= cities.find('a').get_text().strip()
#population_latest=cities.find('td').get_text().strip()

#print(f'City:{city_name}')
#print(f'Latest Population Estimate:{population_latest}')
print(cities)