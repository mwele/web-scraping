from urllib.request import urlopen
from bs4 import BeautifulSoup
html_data=urlopen("https://en.wikipedia.org/wiki/List_of_cities_in_Gabon")
soup=BeautifulSoup(html_data.read(),'lxml')
cities=soup.find_all('tbody')
#cities=cities.get_text()
for el in cities:
    print (el.get_text())
#print(cities)