from bs4 import BeautifulSoup
import requests
html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
#print(html_text)
soup=BeautifulSoup(html_text,'html.parser')
jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    published_date =job.find('span', class_='sim-posted').text
    if 'few' in published_date:
        company_name =job.find('h3',class_= 'joblist-comp-name').text.replace(' ', '')
        skills =soup.find('span',class_='srp-skills').text.replace(' ','')
       # company_name =job.find('h3',class_= 'joblist-comp-name').text.replace(' ', '')
        #print(published_date)
#print(skills)
#print(company_name)
        print(f'''
        Company name: {company_name}
        Required skills:{skills}
        Published Date: {published_date}

        ''')
        print ('-------------------------------------------') #to divide one job from another
