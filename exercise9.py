value = 0
age = 0
while value != -1:
    value = int( input())
    if value>=10 and value<=90:
        if value >= age:
            age = value
print(age)
