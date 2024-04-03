import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', \
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# print logo
print(art.logo)

# caesar cipher function
def caesar(text_to_convert, shift_count, action):

    fully_converted_text = ""

    for char in text_to_convert: # iterate letter by letter

        if char in alphabet:

            char_index = alphabet.index(char) # find index of individual letter

            if action == "encode":
                encode_new_index = char_index + shift_count # encode moves 1 letter up
                fully_converted_letter = alphabet[encode_new_index]
                fully_converted_text += fully_converted_letter

            elif action == "decode":
                decode_new_index = char_index - shift_count # decode moves 1 letter down
                fully_converted_letter = alphabet[decode_new_index]
                fully_converted_text += fully_converted_letter

        # if character is NOT a letter (meaning it's either a number or symbol of some sort), do not convert in any way and just add to string to be printed.
        elif char not in alphabet:
            fully_converted_text += char
            
    print(f"\nThe {action}d text is: {fully_converted_text}")
    print ("\n" + "-" * 80)


# inputs
should_repeat = True
while should_repeat == True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))

    if shift > 26:
        shift = shift % 26
    # e.g. if user enters 27, 27 % 6 = 1, and it shifts by 1 letter

    # Calling Function
    caesar(text_to_convert = text, shift_count = shift, action = direction)

    go_again_ask = input("Would you like to run the cipher program again? [YES] [NO]:\n").lower()

    if go_again_ask == "no" or go_again_ask == "n":
        print("\n[SESSION TERMINATED] Thank you for using the cipher program!")
        print("-" * 80)
        should_repeat = False

    elif go_again_ask == "yes" or go_again_ask == "ye" or go_again_ask == "y":
        print("\n" + "-" * 80)
        should_repeat == True