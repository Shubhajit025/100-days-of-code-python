# Here we need to close the file after open it to free up resources used to speed ip performance of our computer.
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Here no need to close the file.
# To read file
# with open("C:\\Users\\sharm\\OneDrive\\Desktop\\my_file.txt") as file:
# Absolute file path
# with open("/Users/sharm/OneDrive/Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Relative file path
with open("../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)


# To write in file
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

# To write in file by making a new file.
# with open("new_file.txt", mode="w") as trial_file:
#     trial_file.write("New text.")
