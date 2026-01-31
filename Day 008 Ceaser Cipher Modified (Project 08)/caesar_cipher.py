from  art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    final_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for char in original_text:
        if char not in original_text: # I mistakenly not used the 'not', so I faced some bug issue here.
            final_text += char
        else:
            shifted_position = alphabet.index(char) + shift_amount
            shifted_position %= len(alphabet)
            final_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {final_text}")

yes_or_no = True

while yes_or_no:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

    if restart == "no":
        yes_or_no = False
        print("Good Bye.")
