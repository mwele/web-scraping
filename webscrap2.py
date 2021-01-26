import requests
response = requests.get("https://en.wikipedia.org/robots.txt").text
#test = response.text
print("robots.txt for http://www.wikipedia.org/")
print("===================================================")
print(response)
