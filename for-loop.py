"""
for letter in "Giraffe Academy":
    print(letter)
"""

"""
friends = ["Jim", "Karen", "Kevin"]
len(friends)
for index in range(len(friends)):
    print(friends[index])
"""

"""
friends = ["Jim", "Karen", "Kevin"]

for index in range(5):
    if index ==0:
        print("First iteration")
    else:
        print("Not first iteration")
"""

# Exponents
def raise_to_power(bas_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * bas_num
    return result

print(raise_to_power(25, 3))
