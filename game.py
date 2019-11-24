import random
min =1
max = 99
lastAnswer = random.randint(min,max)
print (lastAnswer)

javab = input( )


while javab != 'd':
    if javab == 'b':
        min=lastAnswer
        lastAnswer = random.randint(lastAnswer,max)
        print (lastAnswer)
        javab = input( )
    elif javab == 'k':
        max=lastAnswer
        lastAnswer = random.randint(min,lastAnswer)
        print (lastAnswer)
        javab = input( )

print('hale dadash')

