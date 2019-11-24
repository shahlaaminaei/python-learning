import collections
number = int(input())
list_ara = collections.OrderedDict()

index = 0
while number >= 1:
    number -= 1
    inp = input()
    list_ara[inp] = list_ara.get(inp, 0)+1
list_ara = collections.OrderedDict(sorted(list_ara.items(), key=lambda t: t[0]))

for letter in list_ara.keys():
    print (letter,list_ara[letter])
