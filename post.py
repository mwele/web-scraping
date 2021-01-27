import requests
url = 'http://www.webscrapingfordatascience.com/postform3/'
# No GET request needed?
formdata = {
'name': 'Seppe',
'gender': 'M',
'pizza': 'like',
'haircolor': 'brown',
'comments': ''
}
r = requests.post(url, data=formdata)
print(r.text)