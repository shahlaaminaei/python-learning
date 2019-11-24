sum = 0
win = 0
count = 30
while count > 0:
    score = int( input() )
    sum +=score
    if score == 3:
        win +=1
    count -=1
print(sum,win)





