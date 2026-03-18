# FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt' 👇
# with open("a_file.txt") as file:
#     file.read()

# KeyError: 'non_existent_key' 👇
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError: list index out of range 👇
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError: can only concatenate str (not "int") to str 👇
# text = "abc"
# print(text + 5)


# ------------------- Error Handling ----------------- #
# FileNotFound
# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", mode="w")
#     file.write("Something\n")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")


# ------------------- Error Handling ----------------- #
# ------------------- Raising Exceptions (Error Handling) ----------------- #

# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", mode="w")
#     file.write("Something\n")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error I made up.")

# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")
#
# bmi = weight / height ** 2
# print(bmi)

fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")

try:
    make_pie(3)
except IndexError:
    print("Fruit pie")
