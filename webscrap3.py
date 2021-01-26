from lxml import html
import requests
response = requests.get('http://www.data.gov/').text
#print(response)
doc_gov = html.fromstring(response)
print(doc_gov)
link_gov = doc_gov.cssselect('small a')[0]
print(link_gov)
print("Number of datasets currently listed on data.gov:")
print(link_gov.text)