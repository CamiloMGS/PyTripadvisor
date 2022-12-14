import requests
from bs4 import BeautifulSoup as soup
from random import randint
from time import sleep

uri = "https://www.tripadvisor.com/Hotels-g297474-Bucaramanga_Santander_Department-Hotels.html"

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0"})
response = session.get(uri, timeout=2)

html = response.content

bsobj = soup(response.content, 'lxml')
links= []

for review in bsobj.findAll('a', {'class':'review_count'}):
    a = review['href']
    a = 'https://www.tripadvisor.com' + a
    a = a[:(a.find('Reviews')+7)]+'-or{}'+a[:(a.find('Reviews')+7)]
    links.append(a)
links

reviews = []

for link in links:
    d = [0,1,2,3,4,5]
    print("---------------\n")
    print(link )
    session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0"})
    response2 = session.get(link.format(i for i in d), timeout=2)
    html2 = soup(response2.content, 'lxml')
    sleep(randint (1,5))
    bsobj2 = soup(response2.content, 'lxml')
    for r in bsobj2.findAll('q'):
        reviews.append(r.span.text.strip())
        print("New Review --------------\n")
        print(r.span.text.strip() + "\n")
        
reviews