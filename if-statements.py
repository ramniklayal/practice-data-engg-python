# Basic if statement
"""
is_male = False
is_tall = False


if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")


if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not male and not tall")
"""

# Comparisions
# max number comparision using functions and if statements (!= is not equal, and == is equal)
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(3333, 412, 511))



