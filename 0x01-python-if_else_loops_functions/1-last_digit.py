#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = abs(number) % 10
	if number < 0:
last_number == last_number * -1
	print("Last digit of {} is {} and is ".format(number, last_number), end="")
if last_number > 5:
	print("greater than 5")
elif last_number == 0:
	print("0")
else:
iprint("less than 6 and not 0")
