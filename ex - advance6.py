word_list = {}
num = int(input())

while num  > 0 :
    num -= 1
    words=input().split()
    word_list[words[1].strip()]=words[0].strip()
    word_list[words[2].strip()]=words[0].strip()
    word_list[words[3].strip()]=words[0].strip()
sentence = input().split()
result=""
for word in sentence:
     result+=" "+word_list.get(word,word)
    
print(result.strip())