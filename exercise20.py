members = int(input())
list_team = []
play_num = [int(x) for x in input().split()]
play_num.sort()
for i in range (0,len(play_num)):
    if play_num[i]<=2:
        list_team.append(play_num[i])
print( int(len(list_team)/3))

    
    