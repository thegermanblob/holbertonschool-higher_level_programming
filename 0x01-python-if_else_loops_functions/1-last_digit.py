#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
pos = False
neg = False
print("Last digit of {:d} is".format(number), end=" ")
if number < 0:
    number = number * -1
    neg = True
else:
    pos = True
if number > 10:
    number = number % 10
if number > 5 and pos:
    print("{:.0f} and is greater than 5".format(number))
elif number is 0:
    print("{:.0f} and is 0".format(number))
elif number < 6 or neg:
    if neg:
        print("-", end="")
    print("{:.0f} and is less than 6 and not 0".format(number))

