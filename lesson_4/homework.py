# Homework Lesson 4 - Conditionals

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# ---------------------------------------------------------------------
# Exercise 1: Temperature Classification
# You're developing a weather application. Write a program that takes 
# a temperature in Fahrenheit as input. If the temperature is above 
# 85°F, print "Hot day ahead!".

temperature = int(input("Enter the temperature in Fahrenheit: "))

if temperature > 85:
    print("Hot day ahead!")
else:
    print("Not a hot day ahead!")

# ---------------------------------------------------------------------
# Exercise 2: Grade Classifier
# As a teacher, you want to automate grading. Write a program that
# takes a student's score as input and prints "Pass" if the score is
# 50 or above, otherwise print "Fail".

student_grade = int(input("Enter student's grade: "))

if student_grade >= 50:
    print("Pass")
else:
    print("Fail")

# ---------------------------------------------------------------------
# Exercise 3: Scholarship Eligibility
# Your university offers scholarships based on academic performance.
# Write a program that takes a student's GPA as input. If the GPA
# is greater than or equal to 3.5, print
# "Congratulations, you're eligible for a scholarship!". If it's
# between 3.0 and 3.49, print "You're on the waiting list."
# Otherwise, print "Keep up the good work."

gpa = float(input("Enter your GPA: "))

if gpa >= 3.5:
    print("Congratulations, you're eligible for a scholarship!")
elif 3.0 <= gpa <= 3.49:
    print("You're on the waiting list.")
else:
    print("Keep up the good work.")

# ---------------------------------------------------------------------
# Exercise 4: Shopping Discount
# A store is offering a discount on a product. Write a program that
# takes the original price and the discount percentage as input.
# If the discounted price is less than $50, print "Great deal!".
# Otherwise, print "Might want to wait for a better offer."

original_price = float(input("Enter product original price: "))
discount_percentage = float(input("Enter discount percentage: "))

discount_price = discount_percentage / 100 * original_price
discounted_price = original_price - discount_price

if discounted_price < 50:
    print("Great deal!")
else:
    print("Might want to wait for a better offer.")

# ---------------------------------------------------------------------
# Exercise 5: Movie Night Decision
# You and your friends are deciding on a movie to watch. Write a
# program that takes two movie ratings as input. If both ratings
# are above 7, print "Let's watch both!". Otherwise,
# print "Let's just pick one."

first_movie_rating = int(input("Please, enter your rating of the first movie: "))
second_movie_rating = int(input("Please, enter your rating of the second movie: "))

if first_movie_rating and second_movie_rating > 7:
    print("Let's watch both!")
else:
    print("Let's just pick one.")

# ---------------------------------------------------------------------
# Exercise 6: Restaurant Recommendation
# You're building a restaurant recommendation system. Write a program
# that takes a person's mood (happy or sad) and hunger level
# (high or low) as input. If they're happy and hungry, recommend
# a fancy restaurant. If they're sad and hungry, recommend comfort food.
# For other cases, recommend a casual dining place.

mood_happy = "happy"
mood_sad = "sad"
mood = input(f"Please, enter your mood '{mood_happy}' or '{mood_sad}': ")

hunger_high = "high"
hunger_low = "low"
hunger_level = input(f"Please, enter your hunger level '{hunger_high}' or '{hunger_low}': ")

if mood == mood_happy and hunger_level == hunger_high:
    print("A fancy restaurant is recommended")
elif mood == mood_sad and hunger_level == hunger_high:
    print("Comfort food is recommended")
else:
    print("A casual dining place is recommended")

# ---------------------------------------------------------------------
# Exercise 7: Exercise 7: Tax Bracket Calculator
# You're building a tax calculation system. Write a program that
# takes a person's annual income as input. Use nested conditionals
# to determine their tax bracket based on the following rules:

# - If income is less than $40,000, tax rate is 10%.
# - If income is between $40,000 and $100,000 (inclusive), tax rate is 20%.
# - If income is greater than $100,000, tax rate is 30%.
#
# Print the calculated tax amount for the given income.

annual_income = int(input("Enter annual income: "))

if annual_income:
    if annual_income <= 40000:
        tax_rate_10 = annual_income * 0.1
        print("Tax rate is 10%")
        print(f"Tax amount: {tax_rate_10}")
    if 40000 < annual_income <= 100000:
        tax_rate_20 = annual_income * 0.2
        print("Tax rate is 20%")
        print(f"Tax amount: {tax_rate_20}")
    if annual_income > 100000:
        tax_rate_30 = annual_income * 0.3
        print("Tax rate is 30%")
        print(f"Tax amount: {tax_rate_30}")

# ---------------------------------------------------------------------
# Exercise 8: Ticket Pricing System
# You're working on a ticket booking system for an amusement park.
# Write a program that takes a person's age as input and determines
# their ticket price based on the following rules:
# - Children (ages 3 to 12): $10
# - Adults (ages 13 to 64): $20
# - Seniors (ages 65 and above): $15
# Print the calculated ticket price for the given age.

age = int(input("Enter your age: "))

if 3 <= age <= 12:
    print("Children: $10")
elif 13 <= age <= 64:
    print("Adults: $20")
elif 65 <= age:
    print("Adults: $15")
else:
    print("Free ticket")

# ---------------------------------------------------------------------
# Exercise 9: Password Strength Checker
# Create a program that takes a password as input and checks its
# strength based on the following rules:

# If the password is less than 8 characters, print "Weak password."
# If the password is 8 to 12 characters long, print "Moderate password."
# If the password is more than 12 characters, print "Strong password."

password = input("Enter your password: ")

if len(password) < 8:
    print("Weak password.")
elif 8 <= len(password) <= 12:
    print("Moderate password.")
else:
    print("Strong password.")

# ---------------------------------------------------------------------
# CHALLENGE: Course Enrollment Eligibility
# To solve this exercise, you will need to use the following concepts
# and methods:
# - String method .upper()
# - String slicing
# - if-elif-else conditional statements
#
# You're designing a course enrollment system. Write a program that
# takes a course code and a student's grade as input and determines
# whether the student is eligible to enroll in the course.

# 1. Ask the user to enter a course code (e.g., "CS101", "MATH202", ).
#    All courses ends with "101", "202" or "303". Slice the string
#    to get the last three character of the string to get the course
#    ending:
#
#    Hint:
#    test = "ABCDEF"  # Given this string
#    print(test[-2:])  # It will print "EF"

# 2. Ask the user to enter their grade (e.g., "A", "B", "C", "D", "F").
#    Use .upper() method to convert the course code and grade to uppercase,
#    allowing for case-insensitive input.
#
# Implement the following enrollment rules:
# - For courses with course codes ending in "101", students with
#   grades "A" or "B" are eligible.
# - For courses with course codes ending in "202", students with
#   grades "B" or "C" are eligible.
# - For courses with course codes ending in "303", students with
#   grades "C" or "D" are eligible.

# Print either "You are eligible to enroll." or "You are not eligible to enroll."
course_code = input("Enter the course code: ")
student_grade = input("Enter your grade: ")

# Convert input to uppercase for case-insensitive comparison

course_code = course_code.upper()[-3:]
student_grade = student_grade.upper()

# Extract the last three characters of the course code

if course_code == str(101):
    if student_grade == "A" or "B":
        print(f"Students with {student_grade} are eligible for courses with course codes ending in {course_code}")
elif course_code == str(202):
    if student_grade == "B" or "C":
        print(f"Students with {student_grade} are eligible for courses with course codes ending in {course_code}")
elif course_code == str(303):
    if student_grade == "C" or "D":
        print(f"Students with {student_grade} are eligible for courses with course codes ending in {course_code}")