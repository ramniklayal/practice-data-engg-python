"""
character_nickname = "Dude"         # text
character_firstname = "Jeffrey"     # text
character_age = 33                  # number
is_male = True                      # boolean
# These 3 types of data are most useful for beginners.
# First two are strings (str), then number (int & float are common ones).
# Third one is boolean, only has True or False values.

print("There was once a man named " + character_nickname + ", ")
print("he was " + str(character_age) + " years old.")
print("He was called " + character_firstname + " by other people, ")
print("but, he didn't like his real name.")
"""

# Working with numbers
# print(3 * (6 +9))

# Modulus
# print(10 % 3)

from math import *

# Printing numbers with strings
# my_num = -5
# print(str(my_num) + " is larger than 4")

# Functions with numbers
# print(pow(4, 6))
# print(max(4, 6))
# print(min(4, 6))
# print(round(3.7))

# Using import math module
# print(floor(3.7))
# print(ceil(3.7))
# print(sqrt(9))

# Input program
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)
