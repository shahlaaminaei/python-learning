import requests
from bs4 import BeautifulSoup
import re
r = requests.get('https://maktabkhooneh.org/')
soup = BeautifulSoup(r.text, 'html.parser')
