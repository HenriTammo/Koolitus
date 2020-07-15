import requests
from bs4 import BeautifulSoup

def soupify(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    return soup

def setRange():
    wish = input("Kas soovid määrata miinimum ja maksimum hinda(y/n)") 
    if wish == "y":
        minPrice = float(input("Sisesta miinimum hind"))
        maxPrice = float(input("Sisesta maksimaalne hind"))
        if minPrice > maxPrice:
            return None, None
        return minPrice, maxPrice
    else:
        return None, None

def priceSpider():
    page = 1
    breakPoint = 0
    query = input("Mida soovid otsida \n")
    minPrice, maxPrice = setRange()
    nimekiri = [None] * 10000
    while breakPoint == 0:
        if minPrice != None and maxPrice != None:
            url = "https://www.hinnavaatlus.ee/search/index/?query="+ query +"&min_price="+ str(minPrice) +"&max_price="+ str(maxPrice) +"&page=" + str(page)
        else:
            url = "https://www.hinnavaatlus.ee/search/index/?query="+ query +"&min_price=&max_price=&page=" + str(page)
        soup = soupify(url)
        for name in soup.findAll("span", {"class" : "name"}):
            text = name.get_text()
            print(text)
        page = page + 1

priceSpider()