from urllib.request import urlopen
from bs4 import BeautifulSoup
html_data=urlopen("https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Ethiopia")
soup=BeautifulSoup(html_data.read(),'lxml')
cities=soup.find_all('tr')
#cities=cities.get_text()
for el in cities:
    print (el.get_text())
#print(cities)