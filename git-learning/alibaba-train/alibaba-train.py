import requests
import json
dic_yata_code = {"تهران":"THR","مشهد":"MHD","یزد":"AZD","شیراز":"SYZ","بندرعباس":"BND","اهواز":"AWZ"}
departure_city = input("Please enter departure city: ")
arrival_city = input("Please enter arrival city: ")
departure_date = input("Please enter departure date, exmple(1398-09-25): ")
num_travellers = input("Please enter number of travellers: ")

url = ('https://www.alibaba.ir/train/'+dic_yata_code[departure_city]+'-'dic_yata_code[arrival_city]+'?adult='+num_travellers+'&child=0&infant=0&isExclusive=false&ticketType=Family&step=results&departing='+departure_date)
response = requests.get(url)
