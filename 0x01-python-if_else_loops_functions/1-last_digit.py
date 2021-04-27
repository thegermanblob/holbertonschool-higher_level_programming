#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
neg = True
print("Last digit of {:d} is ".format(number), end="")
if number < 10 and number > -10:
    print("{:d}".format(number), end="")
if number < 0:
    print("-", end="")
    number = number * -1
    neg = False

number = number % 10

if number > 5 and neg:
    print("{:.0f} and is greater than 5".format(number))
elif number is 0 and neg:
    print("{:.0f} and is 0".format(number))
elif number < 6 or neg:
    print("{:.0f} and is less than 6 and not 0".format(number))

