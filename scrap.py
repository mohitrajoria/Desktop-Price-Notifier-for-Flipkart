import requests
from bs4 import BeautifulSoup



def get_price(product_address):
    driver = requests.get(product_address)

    content = driver.content
    # print(content)
    soup = BeautifulSoup(content,'html.parser')
    x = soup.find(class_="_1vC4OE _3qQ9m1").get_text()
    return x

# print(get_price(product_address))
