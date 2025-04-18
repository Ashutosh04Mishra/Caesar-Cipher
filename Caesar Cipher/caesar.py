from image import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode) :

    cipher_text = ""

    if encode_or_decode == "decode" :
        shift_amount *= -1

    for letter in original_text :

        if letter not in alphabet :
            cipher_text += letter

        else :

            shift_position = alphabet.index(letter) + shift_amount
            shift_position %= len(alphabet)

            cipher_text += alphabet[shift_position]

    print(f"The {encode_or_decode}d code is : {cipher_text}")


continue_caeser = True
while continue_caeser:
    direction = input("Type 'encode' to encrypt or type 'decode' to decrypt.\n").lower()
    text = input("Enter text : ").lower()
    shift = int(input("Enter shift amount : "))

    caesar(text,shift,direction)  

    cont = input("Type 'yes' if you want to continue or 'no' to stop.\n")
    if cont == 'no':
        break