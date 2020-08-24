# 
# a1pr1.py - Assignment 1, Problem 1
#
# Indexing and slicing puzzles
#
# This is an individual-only problem that you must complete on your own.
# 

#
# List puzzles
#

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example puzzle (puzzle 0):
# Creating the list [2, 5, 9] from pi and e
answer0 = [e[0]] + pi[-2:] 
print(answer0)

# Solve puzzles 1-4 here:

# Puzzle1
# Creating the list [2, 7] from pi and e
answer1 = e[:2]
print(answer1)

# Puzzle2
# Creating the list [5, 4, 3] from pi and e
answer2 = pi[-2::-2]
print(answer2)

# Puzzle3
# Creating the list [3, 5, 7] from pi and e
answer3 = [pi[0], pi[-2], e[1]]
print(answer3)

# Puzzle4
# Creating the list [1, 2, 3, 4, 5] from pi and e
answer4 = e[-1::-2] + pi[::2]
print(answer4)



#
# String puzzles
#

b = 'boston'
u = 'university'
t = 'terriers'

# Example puzzle (puzzle 5)
# Creating the string 'bossy'
answer5 = b[:3] + t[-1] + u[-1]
print(answer5)

# Solve puzzles 5-10 here:
# Puzzle6
# Creating "universe" from b, u and t
answer6 = u[:-3] + t[1]
print(answer6)

# Puzzle7
# Creating "roster" from b, u and t
answer7 = t[2] + b[1:4] + t[-3:-1]
print(answer7)

# Puzzle8
# Creating "boisterous" from b, u and t
answer8 = b[:2] + t[4::3] + t[:3] + b[1] + u[::6]
print(answer8)

# Puzzle9
# Creating "yesyesyes" from b, u and t
answer9 = (u[-1] + t[-3::2]) * 3
print(answer9)

# Puzzle10
# Creating "trist" from b, u and t
answer10 = t[:-3:2] + b[2:4]
print(answer10)

