"""
This program takes a user input as a number and then runs it through a set of condtionals
to determine if it is positive, negative, or a zero.
"""

num = int(input("Enter a number: "))

if num > 0:
    print("That number is positive!")
elif num < 0:
    print("That number is negative!")
else:
    print("That number is zero!")