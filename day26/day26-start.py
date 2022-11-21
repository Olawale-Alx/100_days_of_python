import random
import pandas


# List comprehension with Strings
# name = 'Olawale'
# new_list = [n for n in name]
# print(new_list)

# List comprehension with rangge of numbers
# items = []
# for a in range(1, 5):
#     a *= 2
#     items.append(a)
# print(items)
# item_in_range = [i * 2 for i in range(1, 5)]
# print(item_in_range)

# List comprehension with if condition
# name = input('Enter your name:\n')
# name_list = [letter for letter in name if (name != 'ola')]
# print(name_list)

# List comprehension extracting variables from a list using if condition
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# name_list = [name.upper() for name in names if (len(name) > 5)]
# print(name_list)

# List comprehension square numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num * num for num in numbers]
# print(squared_numbers)

# List comprehension extracting even numbers only with if condition
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# even_numbers = [num for num in numbers if (num % 2 == 0)]
# print(even_numbers)

# List comprehension reading two files and writing similar numbers to a list with if condition
# with open('./file1.txt', mode='r') as file1:
#     first_file = file1.readlines()
#     # print(first_file)
# with open('./file2.txt', mode='r') as file2:
#     second_file = file2.readlines()
# results = [int(num) for num in first_file if (num in second_file)]
# print(results)

# student_1 = {'name': 'Olawale', 'age': 25, 'class': 'HND2', 'year': 2016}
# for key, value in student_1.items():
#     print(f'{key}: {value}')
# key_value = {key: value for key, value in student_1.items()}
# print(key_value)

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# student_scores = {key: random.randint(30, 100) for key in names}
# print(student_scores)
# passed_students = {key: value for key, value in student_scores.items() if (value >= 60)}
# print(passed_students)
# top_student = {key: value for key, value in student_scores.items() if (value == max(student_scores.values()))}
# print(f'{top_student}')

# sentence = 'What is the Airspeed Velocity of an Unladen Swallow?'
# sentence_list = sentence.split()
# list_count = {word: len(word) for word in sentence_list}
# print(list_count)

# weather_c = {
#     'Monday': 12,
#     'Tuesday': 14,
#     'Wednesday': 15,
#     'Thursday': 14,
#     'Friday': 21,
#     'Saturday': 22,
#     'Sunday': 24
# }
#
# weather_f = {key: (value * 9/5) + 32 for key, value in weather_c.items()}
# print(weather_f)

students_dict = {
    'student': ['Angela', 'James', 'Lily'],
    'score': [56, 67, 98]
}
students_df = pandas.DataFrame(students_dict)
print(students_df)
# for (index, row) in students_df.iterrows():
#     if row.student == 'Angela':
#         print(row.score)
students_row = {index: row for (index, row) in students_df.iterrows() if (row.student == 'Angela')}
print(students_row)

