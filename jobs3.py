from bs4 import BeautifulSoup
import requests
unfamiliar_skill =input('>')
unfamiliar_skill2=input('>')
print(f'Filtering out {unfamiliar_skill},{unfamiliar_skill2}')
html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
#print(html_text)
soup=BeautifulSoup(html_text,'html.parser')
jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    published_date =job.find('span', class_='sim-posted').span.text
    if 'few' in published_date:
        company_name =job.find('h3',class_= 'joblist-comp-name').text.replace(' ', '')
        skills =job.find('span',class_='srp-skills').text.replace(' ','')
        more_info =job.header.h2.a['href']
        if unfamiliar_skill not in skills:
            print(f"company name:{company_name.strip()} ") #strip() removes blank spaces
            print(f"Required skills:{skills.strip()}")
            print(f"More info:{more_info}")

            print ('-------------------------------------------') #to divide one job from another
        elif unfamiliar_skill2 not in skills:
            print(f"company name:{company_name.strip()} ") #strip() removes blank spaces
            print(f"Required skills:{skills.strip()}")
            print(f"More info:{more_info}")

            print ('-------------------------------------------')
