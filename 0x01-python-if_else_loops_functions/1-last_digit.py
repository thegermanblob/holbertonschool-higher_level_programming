#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
pos = True
neg = False
num = abs(number) % 10
print("Last digit of {:d} is".format(number), end=" ")
if number < 0:
    number = num * -1
    neg = True
    pos = False
if num > 5 and pos:
    print("{} and is greater than 5".format(num))
elif num is 0:
    print("{} and is 0".format(num))
elif num < 6 or neg:
    if neg:
        print("-", end="")
    print("{} and is less than 6 and not 0".format(num))

