import math
from math import sqrt
num = int(input())
list_num = []
while num >=1:
    num -= 1
    num_sqrt = int(input())
    list_num.append(str(sqrt(num_sqrt)))
print(*list_num, sep="\n")
