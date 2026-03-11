import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_df = pandas.DataFrame(data)

nato_dict = {row.letter:row.code for (index, row )in nato_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter your name: ").upper()

name_list = [letter for letter in user_input]
nato_list = [nato_dict[char] for char in name_list]

print(nato_list)
