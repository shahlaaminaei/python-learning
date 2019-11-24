input_num = int(input())
list_winers = []

while input_num > 0:
    input_num -= 1
    list_winers.append(input().split("."))
for i in range (0,len(list_winers)):
    list_winers[i][1] = list_winers[i][1].capitalize()
list_winers = sorted(list_winers, key=lambda t: (t[0],t[1]))
for row in list_winers:
    print(" ".join(row),sep="\n")

    

