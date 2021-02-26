from lxml import etree
from lxml import html
import requests
html_page =requests.get('https://www.whoscored.com/Statistics').text 
tree=html.fromstring(html_page)
print(tree)
for tr in tree.xpath('//*[@id="top-team-stats-summary-content"]/tr'):
    print(tr)