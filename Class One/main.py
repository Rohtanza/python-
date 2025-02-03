
# compiler vs interpreter
# compiler == file code = (rust, c, cpp) binary (01010101010) == machine lang  compiler == 100 percent code is converted to binary before running
# interpreter python == line by line code run == high level lang
# py to c/cpp to machine code
# which one is fast c vs python?
# extra level of abstraction
# reason static vs dynamic ? c static
#--------------------------------------------------

# 2 3 4 5 6 = nums
# a b c d = character

# ----
x = 'A' # statement of code
y = 'B'
# print built = print on console
print ("Hello World")
print (x)
print ('y')
#####

# control flow (indent)
if x == y:
    print("x is equal to y")
    print("Continue")
    print("Continue")
    if x == y:
        print("Continue")

# semicolon is ending statement
# three statement
a = 5;b = 11;c = 10

# backslash is dividing single line of code into two line
sum = 1 + 2 + 3 + 4 + 5 \
      + 6 + 7 + 8 + 9 + 10
print(sum)

total = (
    1 + 2 + 3 + 4 +
    5 + 6 + 7 + 8 +
    9 + 10
)
print(total)

# precedent ()

z = 2 + 3 + (1 + 2)
print(z)

f = 2 - 2 + 3 * 2

# %, * and / first
# + and -

# comments (in line comment)

"""

This is the first class of the python 

"""

# first line of comment
# second line of comment


x =  'A'
z = "list, line of chars is called string"

print(f)
# identifier
x = 100
x = 120
X = 130
print(x)
print(X)
# py case sensitive
Ab = 10
ab = 10
aB = 10
aB = 10

# keywords if condition, False, Ture, else, for
# if = 10 wrong

# Rules to name a variable
#     A-Z and a-z 1 2 3 34 5 5
# variable should start with an alphabet

car_one = 100
carOne = 200
CAR_ONE = 200

"""
    conventions to name a variable
    Sample = personone 
        1. snake_case
        example = person_one
        2. camelcase
        example = personOne
        3. ALL_caps
        example = PERSON_ONE
"""

# expressions, operators and operands

"""
    expression = piece of code which returns a value
        x = 2 + 3 # returning the value of 5 to x
    arithmetic operator:
        +, -, *, /, //, %, **
        2 + 3, 2 * 5 , 9 / 3
    Comparison operator:
        1. x == y
        2. x > y
        3. x < y
        4. x >= y (run x is greater or equal to y )
        5. x <= y (run x is less than y )
        6. x != y (run x is not equal to y )     ! = negation  
    Logical operator:
        and, or and not
    
        
"""
print(x)

print(y)

# input taking from the user

name = input("What is your name?")
print("the name is:", name)


