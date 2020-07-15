import requests
from bs4 import BeautifulSoup

def soupify(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    return soup

def getPrice(url):
    price = soupify(url)
    priceString = price.find("p", {"class": "object-price-value"})
    priceString = priceString.get_text() 
    return priceString

def kv():
    page = 1
    breakpoint = 0
    items = [None] * 1000
    query = input("Mida me otsime")
    url = "https://www.kv.ee/?act=search.simple&page="+ str(page) +"&orderby=ob&deal_type=1&dt_select=1&search_type=old&keyword=" + query
    soup = soupify(url)
    while breakpoint == 0:
        for container in soup.findAll("h2", {"class" : "object-title text-truncate"}):
            for name in container.findAll("a", {"class" : "object-title-a text-truncate"}):
                aadress = name.get_text()
                print(aadress, end = "")
                print (getPrice(url))
        page += 1

kv()