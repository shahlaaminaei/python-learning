answer = 0
temp_1 =0
count = 0

for i in range(1,2):
 number = int(input(''))

 for x in range(2, number+1):
    if number % x == 0:
        temp_1+=1
    else:
        x = x + 1

    if temp_1 > count:
        count = temp_1
        answer = number

    elif temp_1 == count:
        if(number > answer):
            answer = number
            count = temp_1

 temp_1 = 0

print(answer, count)