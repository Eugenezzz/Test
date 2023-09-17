# coded_message = 'evif@hgih'
# print(coded_message[-4::-1] + coded_message[3::-1])
# print(coded_message[3::-1])

# age = int(input('Enter your age: '))
#
# if age >= 18:
#     print("You're eligible to vote")
# else:
#     print("You're not eligible to vote yet")

# age = int(input('Enter your age: '))
# message = "eligible" if age >= 18 else "not eligible"
# print(f"You are {message}")

# score = int(input('Enter Score: '))
#
# if score > 0:
#     if score > 90:
#         print('Excellent')
#     elif score >= 70 and score <= 90:
#         print('Good job!')
#     elif score < 70:
#         print('Keep working hard!')
# else:
#     print('No test score available')

# number = 123
#
# if number % 2 == 0:
#     print('even number')
# else:
#     print('odd number')

# number = 15

# if number % 3 == 0:
#     print('Fizz')
# elif number % 5 == 0:
#     print('Buzz')
# elif number % 3 == 0 and number % 5 == 0:
#     print('FizzBuzz')

n = int(input('Enter a number: '))
s = str(n)
if s[0] == '-':
    print('-' + str(s[::-1]))
else:
    print(s)