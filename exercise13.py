jam_moalem = input()
word = []

for num in jam_moalem:
    if num != '+':
        word.append(num)

x = len(word)

for i in range(0,x):
    for j in range(0,x):
        if word[i]<word[j]:
            word[i],word[j]=word[j],word[i]

print("+".join(word))