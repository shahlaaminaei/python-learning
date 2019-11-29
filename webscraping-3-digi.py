import requests
import re
from bs4 import BeautifulSoup
import re
import csv
result=[]

r = requests.get('https://www.digikala.com/incredible-offers/')
soup = BeautifulSoup(r.text, 'html.parser')
all_pro = soup.find_all("div", attrs={"class":"c-product-box c-product-box--product-card c-product-box--has-overflow"})
for pro in all_pro:
    title = pro.find('div',attrs={"class":"c-product-box__title"})
    discount = pro.find('div',attrs={"class":"c-price__discount-oval"})
    sale_price = pro.find('div',attrs={"class":"c-price__value-wrapper"})   
    if title != None and  discount!= None:
        result.append((title.text.strip(),discount.text.strip(),re.sub(',','.',sale_price.text.strip())))
        print(result)
    if discount != None:
        with open("C:\\Users\\shahla\\Desktop\\python\\digikala.csv","w", encoding="utf-8") as f:
            writer = csv.writer(f)
            f.write("title"+','+"discount"+','+"sale_price"+"\n")
            for item in result:
                f.write(str(item[0])+","+str(item[1])+","+str(item[2])+"\n")
            f.close()

            
