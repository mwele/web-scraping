import requests
from bs4 import BeautifulSoup
html = requests.get("https://www.nba.com/standings").text
soup = BeautifulSoup(html, "lxml")
#print(soup.body.div.thead.tbody.tr.td)
#print(str(soup.html.body.div.table)[:100]) #printing the first 100
#table =soup.find_all('id', {'id' ,'__next'})
#tr=[str(tr)[:50] for tr in soup.findAll("tr")]
'''items = dict()
planet_rows = soup.findAll('div', {"class":'#__next '})
for i in planet_rows:
    tds = i.findAll("td")
    items[tds[1].text.strip()] = tds[2].text.strip()
print(tr)'''
from lxml import html
import requests
page_html = requests.get('https://www.soccerstats.com/latest.asp?league=england').text
tree=html.fromstring(page_html)
'''for i in tree:
    print(tree)'''
#print([tr for tr in tree.xpath('//*[@id="btable"]/tbody/tr ')])
for tr in tree.xpath('//*[@id="btable"]/tbody/tr'):
    print (tr)
from lxml import etree
print(etree.tostring(tr[:50]) for tr in tree.xpath('//*[@id="btable"]/tbody/tr'))
