import datetime
from datetime import date, timedelta

def calculateAge(birthDate): 
    
    age = (date.today() - birthDate) // timedelta(days=365.2425)
    return age 

birthday_list = [int(x) for x in input().split("/")]
if birthday_list[1] > 12 or birthday_list[2] > 31:
    print("WRONG")
else: print(calculateAge(date(birthday_list[0], birthday_list[1], birthday_list[2]))) 

