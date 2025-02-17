# old concepts
# interpreter ? dynamic and static type
# high level vs low level language?
# dynamic type , variable datatype
import random
import sys

# 1. casting (low - side)
a = int(2)  # number
b = 3.2  # float
c = "2.2"  # String

# 2. input( parameter )
# return type of the function input() == String
print(a + a)
print(b + b)

# we will use the concept of casting
# d = input("Enter the value of d:")
# print((float(d)))
# int vs float
# int = 1 2 3 4 5 6 7
# float = 1.1, 2.2. 3.4 . 6.5

x, y = 2, 4
# concept
print(x + y)
print("x+y")

# 3.  python multi values assignment

# m = 1
# n = 2
# u = 3
# m, n = "This", 2
# print(m+n)
# we cant perform arm maths ops on different datatypes
# m, n = 2, 2.2
# print(m+n)

# Datatypes:

# str, int, float, boolean,
# boolean = True(anyvalue other then 0 is true) or False(only 0 is false)

# x = bool(00000)
# print(x)

# randon numbers, to generate randoms

# print from 0 to 9
x = random.randrange(0, 10)

# string functions
# slicing string

# print(string[0:2])
# print(string[:2])
# print(string[5:])
#
# print(string.lower())
# print(string.upper())
#
# print(string.capitalize())

string = "        WOW This is a sample string         "

# user input, user put useless spaces in the start of in the end

print(string)
secondString = string.strip()
print(secondString)
# strip white spaces remove, print function string handle white include, but strip
# removes the end or start white spaces

print(sys.getsizeof(secondString))
print(sys.getsizeof(string))

# replace
name = "Rehan"
print(name.replace("", "Zehan"))

secondname = "Python"
print(secondname.split("e"))
# we had to add manually the space b/w string
thirdString = (name + " " + secondname)
print(thirdString)


