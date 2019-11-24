word_list = {}
num = int(input())

while num >= 1:
    num -= 1
    words=input().split()
    word_list[words[0]]=words[1]

sentence = input().split()
result=""
for letter in sentence:
    result+=" "+word_list.get(letter,letter)
    
print(result.strip())