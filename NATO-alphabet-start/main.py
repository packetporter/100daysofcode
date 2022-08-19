# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     print(row.student)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_file = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_file_dict = {row.letter: row.code for (index, row) in nato_file.iterrows()}
print(nato_file_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("What name do you want to look up: ").upper()
code_name = [nato_file_dict[letter] for letter in user_input]
print(code_name)

