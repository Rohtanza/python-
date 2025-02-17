# let's suppose you need a script and the processes you want to run are run 5 times,
# so the best thing you do is to use a for loop with range(5) (that will run from 0 to 4).
# If the processes are unknown, then you will use a while loop.

# for, it lets you decide the count of how many times it will run
# while, it lets you decide the count on the basis of condition

# while True:
#     x = int(input())
#     if x != 1:
#         print("Hello World")
#     else:
#         pass

# x = int(input())
# i = 1
# # x = 5, 1 < 5 == True, now "i" is 2, 2 < 5 == True, i is now 3, 3 < 5, i will be 4, then 4 < 5, i is 5, 5<=5, 6
# while i <= x:
#     print(i)
#     i = i + 1

# -------------------------------------

i = 1
while i <= 10:
    i = i + 1
    if i == 5:
        continue
    print(i)
else:
    print("Finished")

# 2 ways to not print 5
# hint: continue, another hint is if
