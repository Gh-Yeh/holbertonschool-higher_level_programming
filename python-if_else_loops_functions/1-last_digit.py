#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0) and (number*-1) % 10 != 0:
    print(
        f"Last digit of {number} is -{(number*-1) % 10} and is less than 6 and not 0")
elif number % 10 == 0:
    print(f"Last digit of {number} is 0 and is 0")
elif (number % 10 < 6) and number % 10 != 0:
    print(
        f"Last digit of {number} is {number % 10} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {number % 10} and is greater than 5")
