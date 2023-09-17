# name = "Emily"
# age = 26
# job_title = "QA Manager"
# print("{0} and {1}".format("Alice", "Bob"))
# ...print(f"{name} is a {age} + 'years old'")
# "{first_name} and {second_name}".format(first_name = 'Alice', second_name = 'Bob')

# temperature = 25
# f"Temperature is {temperature} C".format(temperature = temperature)

# sentence = "This is a Python Class"
# print(sentence.lower())
# print(sentence.upper())
# print(sentence.title()) #Заглавные буквы у слов
# print(sentence.replace('Python', 'JavaScript'))
# print(sentence.count('i')) #Считает сколько символов
# print(len(sentence)) #возвращает общее число символов

# text = input("Enter the text to be formatted")
#
# print("Uppercase: ".format(text.upper()))
# print("Lowercase: ".format(text.lower()))
# print("Title: ".format(text.title()))
# print("Lowercase: ".format(len(text)))

# word = "Python"
# print(word[::-1])
# print(word[5:2:-1])


def reverse(word):
    return (word[::-1])

print(reverse('Python'))


input_number = -324
num_str = str(input_number)
reversed_str = num_str[:0:-1]
reversed_num = int(num_str[0] + reversed_str)
print(reversed_num)