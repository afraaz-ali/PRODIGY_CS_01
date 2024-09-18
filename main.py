def caesar_cipher(text, shift, mode='encrypt'):
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    result = ''
    for char in text:
        # Check if character is an uppercase letter
        if char.isupper():
            # Shift within uppercase letters (A-Z)
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            # Shift within lowercase letters (a-z)
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Non-alphabetic characters remain unchanged
            result += char

    return result

def main():
    # Get user input
    password = input("Enter the password: ")
    shift = int(input("Enter the shift value: "))
    mode = input("Do you want to encrypt or decrypt? (enter 'encrypt' or 'decrypt'): ").strip().lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
        return

    # Perform encryption/decryption
    result = caesar_cipher(password, shift, mode)

    # Output the result
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
