import requests
from bs4 import BeautifulSoup
import re
r = requests.get('https://maktabkhooneh.org/')
soup = BeautifulSoup(r.text, 'html.parser')
all_pro = soup.find_all("div", attrs={"class":"course-card__description"})
for pro in all_pro:
    badge = pro.find('div',attrs={"class":"course-card__badge--PLUS"})
    uni = pro.find('div',attrs={"class":"course-card__uni"})
    if badge != None and uni != None:
        if badge.text.strip()== "مکتب‌پلاس".strip():
            if uni.text.strip() == "مکتب‌خونه":
                title = pro.find('div',attrs={"class":"course-card__title"})
                print(title.text)
