
#
"""
if some_condition:
    suite_statement_1
    ..
    ..
    ..


"""

number = int(input('Enter a number between 1 and 100:'))
target = 50

if number < target:
    print(number,"is less than",target)
else:
    print(number,"is greater than or equal to",target)


# elif

value = int(input('Enter a number between 1 and 100:'))

print(value,end=" is ")

if value <= 5:
    print("less than or equal to 5")
elif value <= 10:
    print("between 6 and 10 inclusively")
elif value <= 15:
    print("between 11 and 15 inclusively")
else:
    print("greater than 15")

# <, <=, >, >=, ==, !=, is, is not
# not, and, or

x = y = 0
if x == 0 and y == 0:
    pass

if x == 0 or y == 0:
    pass

if not (x == 0 or y == 0):
    pass

