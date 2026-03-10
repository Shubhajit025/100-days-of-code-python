#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.readlines()
    # print(names)

with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    letter = file.read()
#     print(letter)
#Replace the [name] placeholder with the actual name.
for name in names:
    stripped_name = name.strip()
    new_letter = letter.replace("[name]", stripped_name)
#Save the letters in the folder "ReadyToSend".
    with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as file:
        file.write(new_letter)
    # with open(f"Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as file:
    #     file.write(new_letter) -> *This docx file become corrupt
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

