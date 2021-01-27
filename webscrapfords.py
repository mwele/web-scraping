import requests
url = 'http://www.webscrapingfordatascience.com/basichttp/'
r = requests.get(url)
#print(r.content)
print(r.status_code)
# What is the textual status code?
print(r.reason)
# What were the HTTP response headers?
print(r.headers)
print(r.request)
# What were the HTTP request headers?
# The HTTP response content:
print(r.text)