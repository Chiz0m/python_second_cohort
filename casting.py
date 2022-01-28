# casting is the convertion of one data type to another
# integer, float, string, boolean

integerA = 4 # is alread an inger
floatB = 5.9
stringC = "300"
booleanD = False

# int(), float(), str()

# convert from integer to float
newFloat = float(integerA)
# print(type(newFloat))

# convert from integer to string
newString = str(integerA)
# print(type(newString))

# convert from string to ingeter
newInt = int(stringC)
# print(newInt + 100)


# *
# *
# *
# *
# *
# *
# *
# *

# our program is going to allow us to calculate the age of 
# our user

# steps to calculating the age of a user:
# 1. ask for the birth year of the user
# 2. subtract the birth year from the current year
# 3. print the age of the user

birthYear = int(input('What is your birth year: '))
currentYear = 2022
age = currentYear - birthYear
print(f'you are {age} years old and you are born on {birthYear}. Welcome to {currentYear}')

# () this is used to pass arguments
# {} this one is what we use for f string
