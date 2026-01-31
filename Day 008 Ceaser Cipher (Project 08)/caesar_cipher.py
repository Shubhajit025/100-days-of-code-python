print("Welcome to Ceaser Cipher Encryption. 🔒")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):

    encrypted_text = ""

    for char in original_text:
        shifted_text = alphabet.index(char) + shift_amount
        shifted_text %= len(alphabet)
        encrypted_text += alphabet[shifted_text]

    print(f"Your encripted text is : {encrypted_text}")
    
encrypt(original_text=text, shift_amount=shift)
