
userInput = [int(x) for x in input().split()]
mx = max(userInput)
mn = min(userInput)
print(int(abs(mx - userInput[1]) + abs(mn - userInput[1])))


