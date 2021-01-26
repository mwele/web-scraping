from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import requests
#html_text=requests.get("https://www.w3schools.com/python/trypython.asp?filename=demo_try_except2").text
#soup=BeautifulSoup(html_text,'lxml')
try:
    html = urlopen("https://www.w3schools.com/python/trypython.asp?filename=demo_try_except2")
except HTTPError as e:
    print("HTTP error")
except URLError as e:
    print("Server not found!")
else:
    print('Website is found')
try:
    html = urlopen("http://www.example.com/")
except HTTPError as e:
    print("HTTP error")
except URLError as e:
    print("Server not found!")
else:
    print("HTML Details")    
    print(html.read())  
