# cipher code

letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")

def encode(text, shift):
    new_text = ""
    for letter in text:
        position = letters.index(letter)
        new_position = position + shift
        new_text += letters[new_position]
    return new_text
    
def decode(text, shift):
    origanl_text = ""
    for letter in text:
        position = letters.index(letter)
        origanl_position = position - shift
        origanl_text += letters[origanl_position]
    return origanl_text
    
task = input("Would you like to 'encode' or 'decode' ?\n").lower()
if task == 'encode':
    input_text = input("Enter the word you want to encrypt:\n").lower()
    shift = int(input("Number of the shift.\n"))
    encoded_text = encode(text=input_text, shift=shift)
    print(encoded_text)
elif task == 'decode':
    input_text = input("Enter the word you want to dencrypt:\n").lower()
    shift = int(input("Number of the shift.\n"))
    decoded_text = decode(text=input_text, shift=shift)
    print(decoded_text)
else:
    input("Enter only 'encode' or 'decode'")
