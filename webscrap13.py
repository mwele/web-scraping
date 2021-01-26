#https://bit.ly/2lVhlLX
import requests
from lxml import html
url = 'http://www.state.gov/r/pa/ode/socialmedia/'
doc = html.fromstring(requests.get(url).text)
pinlinks = [a for a in doc.cssselect('a') if 'pinterest.com' in str(a.attrib.get('href'))]
print("The number of Pinterest accounts maintained by U.S. State Department embassies and missions:")
print(len(pinlinks))