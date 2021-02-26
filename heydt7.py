import requests
from bs4 import BeautifulSoup
#def get_planet_data():
html = requests.get("https://www.timeanddate.com/weather/").text
soup = BeautifulSoup(html, "lxml")
    #planet_trs = soup.html.body.div.table.findAll("tr", {"class": "planet"})
cities= soup.find_all("a")
temp= soup.find_all("td",class_='rbi')
time= soup.find_all("td", class_='r')
    #cities= soup.find_all("a")
    #cities= soup.find_all("a")
weather_data = dict()
for a in cities:
    #print (a)
    weather_data['cities'] =a.text
for t in time:
    #print(t)
    weather_data['time'] =t.text
    #print(weather_data['time'])
for m in temp:
    #print(m)
    weather_data['temp']=(m.text)
    #print(weather_data['temp'])
   # def to_dict(tr):
        #tds = tr.findAll("td")
'''weather_data = dict()
weather_data['city'] =a.text.strip()
weather_data['time'] =t.text.strip()
weather_data['temp'] =m.text.strip()'''
        #weather_data['Description'] = tds[4].text.strip()
        #weather_data['MoreInfo'] = tds[5].findAll("a")[0]["href"].strip()
        #return weather_data 
'''planets = [to_dict(tr) for tr in planet_trs]
    return planets
if __name__ == "__main__":
    print(get_planet_data())'''
print(weather_data)
#print(weather_data['temp'])
#print(weather_data['time'])
#print(weather_data['cities'])