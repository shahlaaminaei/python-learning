string = input()
word = 'hello'
temp = []
index=0
for i in range(0,len(word)):
    for j in range(index,len(string)):
        if word[i] == string[j]:
            temp.append(string[j])
            i+=1
            index+=1
            break
        else:
            index+=1
print("YES" if "".join(temp)==word else "NO")
