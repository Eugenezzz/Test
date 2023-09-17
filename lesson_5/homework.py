# Homework Lesson 5 - Workshop - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# Challenge 1
# Make a number Positive
#
# Create a variable called my_number and set it to any integer value.
# Write code to make the number positive if it's negative, and keep it
# as is if it's already positive or zero.

my_number = -5

# Example:
# Input: -3 => Output: 3
# Input: 5 => Output: 5

print(int(abs(my_number)))

# ---------------------------------------------------------------------

# Challenge 2
# BinGo!
#
# If the number is divisible of 3, print “Bin”
# If the number is divisible of 7, print “Go”
# For numbers which are divisible of 3 and 7, print “BinGo”
# Otherwise, print the original number: “{number} is just a number”

number = int(input("enter a number: "))

if number % 3 == 0:
    print("Bin")
    if number % 7 == 0:
        print("Go")
elif number % 3 == 0 and number % 7 == 0:
    print("BinGo")
else:
    print(f"{number} is just a number")

# ---------------------------------------------------------------------

# Challenge 3
# Find the middle number
#
# Given three different numbers x, y, and z, find the number that is neither
# the smallest nor the largest and print it.
#
# Example:
# x = 1, y = 5, z = 3 => Output: 3

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if y < x < z or z < x < y:
    print(f"{x} is a middle number")
elif x < y < z or z < y < x:
    print(f"{y} is a middle number")
elif x < z < y or y < z < x:
    print(f"{z} is a middle number")

# ---------------------------------------------------------------------

# Challenge 4
# Palindrome Numbers
#
# Ask a user to input a number.
# Write a program to check if the given number is a palindrome.
# It should print True if the number is a palindrome and False if it is not.
#
# Palindrome number: 121, 898

number = input("Enter a number: ")

if int(number[::]) == int(number[::-1]):
    print(True)
else:
    print(False)

# ---------------------------------------------------------------------

# Challenge 5
# Reverse a string
#
# You're part of a team working on analyzing customer reviews for a new video game.
# Due to a software glitch, some reviews have been recorded in reverse with punctuation
# at the beginning instead of the end. Your task is to correct these reviews so that they
# are in the correct order and the punctuation is appropriately placed at the end of the
# sentence or word.
#
# Example: "tcefreP!" -> Perfect!

incorrect_review = "tcefreP!"

reverse_review = incorrect_review[::-1]
first_reversed_element = reverse_review[0]
correct_review = reverse_review[1::] + first_reversed_element

print(correct_review)

