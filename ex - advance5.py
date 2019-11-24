result = []
my_list=[]
index=0
i=0
text=input().split()
for word in text:
    if word[0].isupper()==True and "." not in text[index-1]:
        result.append((index+1,word.replace(".","").replace(",","").strip()))
    index += 1
    
if result==[]:
    print("None")
else:
    for i in range (0,len(result)):
        print(str(result[i][0])+":"+result[i][1] )