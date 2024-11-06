imporimport requests
from bs4 import BeautifulSoup

for i in range (1, 20):
    page = requests.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={i}")
    soup = BeautifulSoup(page.text, "html.parser")

    names = soup.findAll("a", attrs={"class":"title"}) # Laptop names
    prices = soup.findAll("h4", attrs={"class":"price float-end card-title pull-right"}) # Laptop prices
    descs = soup.findAll("p", attrs={"class":"description card-text"}) # Laptop descriptions

    for name, price, desc in zip(names, prices, descs):
        print(f"Name: {name.text}\nPrice: {price.text}\nDescription: {desc.text}\n")