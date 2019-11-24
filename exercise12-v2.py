string = input('enter string: ').lower()
seda="aeiou"
result=[]
[result.append(".") if letter in seda else  result.append(letter) for  letter in string]
print("".join(result))