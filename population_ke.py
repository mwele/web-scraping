from urllib.request import urlopen
from bs4 import BeautifulSoup

html_data=urlopen("https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Kenya_by_population")
soup=BeautifulSoup(html_data.read(),'lxml')
cities = soup.find_all('tr')
#cities=cities.get_text()
#print(cities)
for el in cities:
    print(el.get_text())

    #16

'''find_all() returns an array of elements. You should go through all of them and select that one you are need. And than call get_text()

UPD
For example:

    for el in soup.find_all('div', attrs={'class': 'fm_linkeSpalte'}):
        print el.get_text()'''