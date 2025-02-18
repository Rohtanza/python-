# Functions
# user defined functions

def compareStudents(StudentA, StudentB, StudentC):
    if StudentA < StudentB:
        print("StudentA is less than StudentB")
        return 0
    elif StudentA > StudentB:
        print("StudentA is greater than StudentB")
        return 1


# example 1
studentOneMarks = 10
studentTwoMarks = 20
StudentThreeMarks = 30

# A code block that is run when we call it, and it returns a result to us
compareStudents(studentOneMarks, studentTwoMarks)
compareStudents(studentOneMarks, StudentThreeMarks)
compareStudents(studentTwoMarks, studentOneMarks)

# for i in range(3):
#     if studentOneMarks > studentTwoMarks:
#         pass
#     if studentOneMarks < StudentThreeMarks:
#         pass
#     if studentTwoMarks < StudentThreeMarks:
#         pass

# example two
Number = 1
# check even or odd number,
# 1, 3, 5, 7 => odd
# 2, 4, 6, 7, 8 => even

# Coding, there are ways to make our code better
# 1. No repeat of code — sometimes we repeat the same block of code many times.
