from scrapy.selector import Selector
import requests
response = requests.get("http://stackoverflow.com/questions")
selector = Selector(response)
print(selector)
summaries = selector.xpath('//div[@class="summary"]/h3/a/text()')
#print(summaries[:3])
print('#################################################################################')
[x.extract() for x in summaries.xpath('a[@class="question-hyperlink"]/text()')[:10]]
   #print(x.extract())
for i in summaries:
    print (i)
