word = input()
lower_count = 0
upper_count = 0
word_list = []
lenth = len(word)
for i in range (0,len(word)):
    if word[i].islower() == True:
        lower_count += 1
    elif word[i].isupper() == True:
        upper_count += 1
if upper_count > lower_count:
    print(word.upper())
else:
    print(word.lower())
