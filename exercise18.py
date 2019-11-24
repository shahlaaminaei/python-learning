word = input()
index =0
list=[]
flagAB=False
flagBA=False
while index<len(word)-1:
    if word[index].lower()+word[index+1].lower() =="ab":
        flagAB=True
        index+=2
    elif word[index].lower()+word[index+1].lower()=="ba":
        flagBA=True
        index+=2
    else:
     index+=1
if flagAB and  flagBA:
    print("YES")
else:
    print("NO")
