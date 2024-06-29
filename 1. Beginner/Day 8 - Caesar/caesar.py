def caesar(plain_text, shift_amount=1):
    if not plain_text:
        print("Usage: caesar(plain_text, shift_amount)")
    if type(shift_amount) is not int:
        print("Shift amount must be an integer")
    else:
        shift_amount = shift_amount % 26
    

    cyphered_text = ""

    for char in plain_text:
        # For non-alphabet characters, don't change them
        if char.isalpha() == False:
            cyphered_text += char
        # For Lowercase
        elif 97 <= ord(char) <= 122:
            if ord(char) + shift_amount > 122:
                cyphered_text += chr(ord(char) + shift_amount - 26)
            else:
                cyphered_text += chr(ord(char) + shift_amount)
        # For Uppercase
        elif 65 <= ord(char) <= 90:
            if ord(char) + shift_amount > 122:
                cyphered_text += chr(ord(char) + shift_amount - 26)
            else:
                cyphered_text += chr(ord(char) + shift_amount)
    
    return cyphered_text

print(caesar("Billie Jean is not my lover. Jack and Jill went up a hill, Humpty Dumpty fell off the wall. Frieren the Slayer!!! @calvinchan4370", 6))