import requests
from  lxml import html

from bs4 import BeautifulSoup
def get_planet_data():
    #html = requests.get("https://basketball.realgm.com/nba/stats").text
    #soup = BeautifulSoup(html, "lxml")
    html_page=requests.get("https://basketball.realgm.com/nba/stats").text
    tree=html.fromstring(html_page)
    #planet_trs = soup.html.body.div.table.find_all("tr", {"class": "summary"})
    #planet_trs=soup.html.body.div.div.div.table.tbody.tr.td.find_all("a").text()
    for x in tree.xpath("/html/body/div[2]/div[3]/div/table/tbody/tr/td/a/text()"):
        planet_trs=print(x)

    #print(a)
    def to_dict(tr):
        tds = tr.findAll("td")
        planet_data = dict()
        planet_data['Team'] = tds[1].text.strip()
        planet_data['GP'] = tds[2].text.strip()
        planet_data['MPG'] = tds[3].text.strip()
        planet_data['FGM'] = tds[4].text.strip()
        planet_data['FG%'] = tds[5].text.strip()
        planet_data['3PM'] = tds[6].text.strip()
        planet_data['3PA'] = tds[7].text.strip()
        planet_data['3P%'] = tds[8].text.strip()
        planet_data['FTM'] = tds[9].text.strip()
        planet_data['FTA'] = tds[10].text.strip()
        planet_data['FT%'] = tds[11].text.strip()
        planet_data['TOV'] = tds[12].text.strip()
        planet_data['PF'] = tds[13].text.strip()
        planet_data['ORB'] = tds[14].text.strip()
        planet_data['DRB'] = tds[15].text.strip()
        planet_data['RPG'] = tds[16].text.strip()
        planet_data['APG'] = tds[17].text.strip()
        planet_data['SPG'] = tds[18].text.strip()
        planet_data['BPG'] = tds[19].text.strip()
        planet_data['PPG'] = tds[20].text.strip()
        #planet_data['FGM'] = tds[4].text.strip()
        return planet_data
    planets = [to_dict(tr) for tr in planet_trs]
    return planets
if __name__ == "__main__":
    print(get_planet_data())