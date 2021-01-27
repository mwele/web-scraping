import requests
url = 'http://www.webscrapingfordatascience.com/simplejavascript/quotes.php'
# Note that cookie values need to be provided as strings
r = requests.get(url)
print(r.json())