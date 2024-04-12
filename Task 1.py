def caesar_cipher(text, shift, decrypt=False):
    result = ''
    for char in text:
        if char.isalpha():
            # Shift uppercase letters
            if char.isupper():
                if decrypt:
                    result += chr((ord(char) - shift - 65) % 26 + 65)
                else:
                    result += chr((ord(char) + shift - 65) % 26 + 65)
            # Shift lowercase letters
            elif char.islower():
                if decrypt:
                    result += chr((ord(char) - shift - 97) % 26 + 97)
                else:
                    result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Keep non-alphabetic characters unchanged
    return result

def main():
    while True:
        choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
        
        if choice == 'q':
            print("Exiting...")
            break
        
        if choice not in ['e', 'd']:
            print("Invalid choice! Please enter 'e', 'd', or 'q'.")
            continue
        
        text = input("Enter the text: ")
        shift = int(input("Enter the shift value: "))
        
        if choice == 'e':
            encrypted_text = caesar_cipher(text, shift)
            print("Encrypted text:", encrypted_text)
        elif choice == 'd':
            decrypted_text = caesar_cipher(text, shift, decrypt=True)
            print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
