#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number) % 10
print("Last digit of {} is".format(number), end=" ")
if number < 0:
    num = num * -1
if num > 5:
    print("{} and is greater than 5".format(num))
elif num is 0:
    print("{} and is 0".format(num))
else:
    print("{} and is less than 6 and not 0".format(num))
