from lxml import etree
from lxml import html
import requests
html_page =requests.get('http://books.toscrape.com/catalogue/category/books_1/index.html').text 
tree=html.fromstring(html_page)
print(tree)
for tr in tree.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/text()[1]')[1].strip():
    print(tr)
print(etree.tostring(tr)[:3] for tr in tree.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a'))
#print(etree.tostring(tr)[:50] for tr in tree.xpath("//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/parent::*"))
