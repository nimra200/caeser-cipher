CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"

def decrypt_message(secret_message:str, key:int) -> str:
    """ Decrypt a secret message by subtracting the key from each letter.
    Preserve all other symbols in the message.
    Precondition: secret_message is a string and key is an integer.
    
    Sample usage:
    >>> decrypt_message("Ifmmp xpsme", 1)
    "Hello world"  
    """
    result = ""
    key = key % 26
    for letter in secret_message:
        if letter.isalpha(): 
            # convert to letter's ASCII value
            ascii_value = ord(letter) - key
            if (ascii_value < ord('A') and letter in CAPS) or (ascii_value < ord('a') and letter in LOWER):
                # send values less than 'A' back to 'Z'
                ascii_value += 26
            decrypted_letter = chr(ascii_value)
            result += decrypted_letter
        else:
            result += letter

    return result

if __name__ == "__main__":
    secret_message = input("Enter your secret message using only English alphabet. ")
    key_prompt = input("Do you have a key? y/n ")
    if key_prompt == "y":
        key = input("Enter your key: ")
        print( decrypt_message( secret_message, int(key) ) )

    else:
        print("Trying to break the cipher... \n")
        # use all possible keys from 1-25 to decrypt the message
        for i in range(1,26):
            print("KEY: {0}, MESSAGE: {1}".format(i, decrypt_message(secret_message, i)))
