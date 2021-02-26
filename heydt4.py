import requests
from lxml import html
html_page =requests.get('https://basketball.realgm.com/nba/stats').text 
tree=html.fromstring(html_page)
#print(tree)
for tr in tree.xpath('/html/body/div[2]/div[3]/div/table/tbody/tr[1]/td/text()'):
    print(tr)
#print(etree.tostring(tr)[:3] for tr in tree.xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a'))
#print(etree.tostring(tr)[:50] for tr in tree.xpath("//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/parent::*"))
print((v, v.xpath("@name")) for v in tree.cssselect('td.nowrap tablesaw-cell-persist'))
for a in tree.xpath("/html/body/div[2]/div[3]/div/table/tbody/tr/td/a/text()"):
    print(a)
for x in tree.cssselect('td.nowrap tablesaw-cell-persist'):
    print(x)