# loops, sytnax, sementics, meaning loop,
# user, send noti, k seat cancel

# Conditional Statement, if then else, elif
# Compile Time, Interpreter time :
#
# 10 lines of code, code, exactly Flow, print("x") 10 times,
#
# Run time decision, Run time, User Code changes
#
# Code written means == logical finalized
#
# Here our conditional Statement, Code
# Two things which can change the flow of code, or RESULT
#
# Run time
#
# 1. Conditional Statement
# 2. Polymorphic behavior OOP
# the
# factor
# which
# decide
# the
# outcome
# of
# conditional
# statements
# are
#
# 1.
# User
# interaction
# 2.
# Software
# interaction(one
# tool
# to
# tool)

# Syntax, conditional two related
# Conditional Expressions: a===b, a!=b, a>=b  And Logical Operators >, and < or ==
# Expression, interpretur

a = 10
b = 20
# 20 > 10, result,

if b > a:
    print("b is greater than a")
# back working
if 20 > 10:
    print("b is greater than a")
if True:
    print("b is greater than a")

# either, happen or not happen

# Condition will only with the if statement
if b == a:
    print("b is greater than a")
else:
    print("b is greater than a")

# elif
# short-circuiting in programming
if True:
    print("b is greater than a")
else:
    print("b is greater than a")
# our option, options to check multiple conditions.

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is greater than b")
elif a == b:
    print("a is greater than b")
elif a != b:
    print("a is greater than b")
else:
    print("for shit, nothing is nothing")

# ways to use conditional statements, syntax-wise, logic-wise
# 1. one line if (if condition: action)

if a == b:
    print("a is greater than b")

# 2. ternary operator, expression, two operator, and three operands, ternary expression
print("a is greater than b") if a > b else print("b is greater than a")
# two operator if and else, and three expression(operands)

# 3. chained, ternary operations
print("a is greater than b") if a > b else print("b is not greater than a") if a == b else print(
    "b is equal than a") if a != b else print("b is not equal than a")
# explanation: compounding exists, in this state, only expression exists rather than code blocks

# shorting circuiting
x = 10
y = 20
z = 30
print("-----------------")
if y > x or x > z or z > y or x == y and z != y or x != z or z <= y:
    print("y is greater than x")

# second example
if y < x and x > z and z > y and x == y and z != y and x != z and z <= y:
    print("y is greater than x")

# semantics (logic) a computer, language, 90 percent, rust, zig, go
# nested if/else
if x > 10:
    print("x is greater than 10")
    if y > x:
        print("y is greater than x")
        print("y is greater than x")
        print("y is greater than x")
        print("y is greater than x")
        print("y is greater than x")
    elif y < x:
        print("y is greater than x")
        if x == y:
            print("x is equal than y")
    else:
        pass
else:
    print("hurryyyyy!")

# if age is more than 18 than don't say anything, but if the age is underage then say k get out
# bouncer, club,
terriost = False
allowedAge = 18
oldSucker = 20
youngGirl = 12
print("---------------")
if oldSucker >= allowedAge:
    pass
elif youngGirl >= allowedAge:
    pass
else:
    print("get your minor ass out of here")

#-----------------------------------------------
