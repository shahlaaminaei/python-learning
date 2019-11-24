import collections
from collections import OrderedDict

result = OrderedDict()
result = {
    "Iran":{"win":0 , "loses":0 , "draws":0 , "goal difference":0 , "points":0 },
    "Spain":{"win":0 , "loses":0 , "draws":0 , "goal difference":0 , "points":0 },
    "Portugal":{"win":0 , "loses":0 , "draws":0 , "goal difference":0 , "points":0 },
    "Morocco":{"win":0 , "loses":0 , "draws":0 , "goal difference":0 , "points":0 }
    }

list_score = []
matchs = [("Iran","Spain"),("Iran","Portugal"),("Iran","Morocco"),("Spain","Portugal"),("Spain","Morocco"),("Portugal","Morocco")]
for i in range(0,6) :
    meach_result=input().split("-")
    match=matchs[i]
    result[match[0]]["goal difference"]=result[match[0]]["goal difference"]+(int(meach_result[0])-int(meach_result[1]))
    result[match[1]]["goal difference"]=result[match[1]]["goal difference"]+(int(meach_result[1])-int(meach_result[0]))

    if(int(meach_result[0])>int(meach_result[1])):
        result[match[0]]["win"]=result[match[0]]["win"]+1
        result[match[0]]["points"]=result[match[0]]["points"]+3
        result[match[1]]["loses"]=result[match[1]]["loses"]+1
    elif(int(meach_result[0])<int(meach_result[1])):
        result[match[1]]["win"]=result[match[1]]["win"]+1
        result[match[1]]["points"]=result[match[1]]["points"]+3
        result[match[0]]["loses"]=result[match[0]]["loses"]+1
    else:
        result[match[0]]["points"]=result[match[0]]["points"]+1
        result[match[1]]["points"]=result[match[1]]["points"]+1
        result[match[0]]["draws"]=result[match[0]]["draws"]+1
        result[match[1]]["draws"]=result[match[1]]["draws"]+1
result_sorted= sorted(result.keys(), key=lambda x: (-result[x]['points'],x[0][1]))


for item in result_sorted:
    str_result=item+" "
    str_result+="wins:"+str(result[item]["win"])+" , "
    str_result+="loses:"+str(result[item]["loses"])+" , "
    str_result+="draws:"+str(result[item]["draws"])+" , "
    str_result+="goal difference:"+str(result[item]["goal difference"])+" , "
    str_result+="points:"+str(result[item]["points"])+" "
    print(str_result)