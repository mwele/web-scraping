#https://bit.ly/2lVhlLX
# via: https://analytics.usa.gov/
import requests
url = 'https://analytics.usa.gov/data/live/realtime.json'
j = requests.get(url).json()
print("Number of people visiting a U.S. government website-")
print("Active Users Right Now:")
print(j['data'][0]['active_visitors'])