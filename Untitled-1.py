import re
input_email = input()
result = re.search(r"(\w+.*@\w+\w+\.+\w+\w+$)",input_email)
if result != None:
    print("OK")
else:
    print("WRONG")