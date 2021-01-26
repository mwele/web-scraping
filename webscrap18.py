import requests
response = requests.get('https://python.org')
print("Status Code: ",response.status_code)
print("Headers: ",response.headers)
print("Url: ",response.url)
print("History: ",response.history)
print("Encoding: ",response.encoding)
print("Reason: ",response.reason)
print("Cookies: ",response.cookies)
print("Elapsed: ",response.elapsed)
print("Request: ",response.request)
print("Content: ",response._content)
#print(response.json())