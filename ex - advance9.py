import random
from random import randint

class Person:
    def __init__(self, name):
        self.name = name

class Player(Person):
    def __init__(self,name,team):
        super(Player, self).__init__(name)
        self.team = team
    def __repr__(self):
        return '%s %s' %(self.name ,self.team)
def select_random_team (player_list):
    result = []
    for i in range (0,len(player_list)):
        index = randint(1,2)
        if index == 1:
            p=Player(player_list[i],"A")
            result.append(p)
        else:
            p=Player(player_list[i],"B")
            result.append(p)
    return result


print(*select_random_team(["حسین","مازیار","اکبر","نیما", "مهدی","فرهاد","محمد","خشایار","میلاد","مصطفی","امین","سعید","پویا","پوریا","رضا","علی","بهزاد","سهیل","بهروز","شهروز","سامان","محسن"]),sep="\n")
    