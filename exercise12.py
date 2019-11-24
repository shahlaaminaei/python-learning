string = input().lower()
seda="aeiou"
result = ""
for letter in string:
    if letter in seda:
        result = result + "."
    else:
        result = result + letter
print(result)