# List comprehension

# new_list = [new_item for item in list if test]

# new_numbers = [n + 1 for n in numbers]
# name = "Shubhajit"
# name = "Shubhajit"
# new_list = [letter for letter in name]
# new_list = [n * 2 for n in range(1, 5)]
# new_list1 = [n * 2 for n in range(1, 5)]
# new_name = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# new_name
# ['Alex', 'Beth', 'Caroline', 'Dave', 'Elannor', 'Freddie']
# short_name = [name_n for name_n in new_name if len(name_n) < 5]
# long_name = [nama.upper() for nama in new_name if len(nama) > 5]

# Dictionary Comprehension

# new_dict = {new_key:new_value for item in list if test} -> for list to dict
# new_dict = {new_key:new_value for (key, value) in dict.items() if test} -> for dict to dict

# names = ["Alex", "Beth", "Caroline", "Dave", "Elannor", "Freddie"]
# import random
# students_scores = {student:random.randint(1, 100) for student in names}
# passed_students = {key:value for (key, value) in students_scores if value >= 60}
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# ValueError: too many values to unpack (expected 2) got error
# passed_students = {key:value for key, value in students_scores if value >= 60}
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# ValueError: too many values to unpack (expected 2) got error again then solved it
# passed_students = {key:value for key, value in students_scores.items() if value >= 60}

import pandas

student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

student_df = pandas.DataFrame(student_dict)
# print(student_df)

# Looping through DataFrame:
# for (key, value) in student_df.items():
#     print(value)

# Loop through rows of a data frame:
for (index, row) in student_df.iterrows():
    # print(row.score)
    if row.student == "Angela":
        print(row.score)

# {new_key:new_value for (index, row) in df.iterrow()}

# TODO 1: Create a dict in this format = {"A": "Alfa", "B": "Bravo"}
# TODO 2 : Create a list of the phonetic code words from a word  that the user inputs.
