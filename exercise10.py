value = 0
biggest = 0
big = 0
while value != -1:
    value = int( input())
    age2 = value
    if value>=10 and value<=90:
        if value >= big :
            big = value
            if big > biggest:
                big,biggest=biggest,big
  
print(biggest,big)
