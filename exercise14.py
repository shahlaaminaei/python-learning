# count = 0
# name = input()
name_list = []
for i in range(0,10):
    name = input()
    name = name[0].upper() + name[1:].lower()
    name_list.append(name)
print(*name_list, sep="\n")