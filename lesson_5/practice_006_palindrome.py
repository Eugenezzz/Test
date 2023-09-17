# A palindrome is a word, number, phrase, or other sequence of symbols
# that reads the same backwards as forwards:
#
# madam -> madam
# racecar -> racecar
# tacocat -> tacocat
#
# Write a program that will print True if the word is a palindrome
# and False if it is not.

word = str(input('Enter a word: '))

if word == word[::-1]:
    print('palindrome')
else:
    print('not a palindrome')
