number = int(input())
list = []
index = 0
isWin = False
while number >= 1:
    number -= 1
    desc = [int(x) for x in input().split()]
    list.append(desc)
list.sort()
for item in list:
    index += 1
    for next in list[index:]:
        if item[0]<next[0] and item[1]>next[1]:
            isWin=True
            break
if(isWin):
    print("happy irsa")
else:
    print("poor irsa")

