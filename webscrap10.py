from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://en.wikipedia.org/wiki/Python")
bsObj = BeautifulSoup(html,'lxml')
for link in bsObj.findAll("a"):
  if 'href' in link.attrs:
    print(link.attrs['href'])