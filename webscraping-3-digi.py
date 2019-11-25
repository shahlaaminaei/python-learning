import requests
from bs4 import BeautifulSoup
import re
r = requests.get('https://www.digikala.com/incredible-offers/')
soup = BeautifulSoup(r.text, 'html.parser')
all_pro = soup.find_all("div", attrs={"class":"c-product-box c-product-box--product-card c-product-box--has-overflow"})
for pro in all_pro:
    title = pro.find('div',attrs={"class":"c-product-box__title"})
    first_price = pro.find('div',attrs={"class":"c-price__value c-price__value--plp"})
    discount = pro.find('div',attrs={"class":"c-price__discount-oval"})
    sale_price = pro.find('div',attrs={"class":"c-price__value-wrapper"})   
    if discount != None:
        print("title:",title.text.strip(),"\n","discount:",discount.text.strip())