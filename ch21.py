from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html,'lxml')
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
ngrams = ngrams(content, 2)
print(ngrams)
print("2-grams count is: "+str(len(ngrams)))



def ngrams(input, n):
    content = re.sub('\n+', " ", content)
    content = re.sub(' +', " ", content)
    content = bytes(content, "UTF-8")
    content = content.decode("ascii", "ignore")
    print(content)
    input = input.split(' ')
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
        return output
