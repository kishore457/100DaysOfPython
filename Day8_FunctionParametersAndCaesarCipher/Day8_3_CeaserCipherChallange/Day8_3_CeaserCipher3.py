alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction1 = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text1 = input("Type your message:\n").lower()
shift1 = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(text, shift, direction):
    modified_text = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        position = alphabet.index(letter)
        # if direction == "encode":
        #     new_position = position + shift
        #     modified_text += alphabet[new_position]
        # elif direction == "decode":
        #     new_position = position - shift
        #     modified_text += alphabet[new_position]
        new_position = position + shift
        modified_text += alphabet[new_position]
    print(f"{direction1} text is : {modified_text}")

caesar(text =text1, shift = shift1, direction = direction1 )

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.