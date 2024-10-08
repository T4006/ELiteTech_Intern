def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
            
    return result

def main():
    while True:
        try:
            # Ask user whether to encrypt or decrypt
            action = input("Would you like to (E)ncrypt or (D)ecrypt? ").strip().upper()

            if action not in ['E', 'D']:
                print("Invalid option. Please enter 'E' for encrypt or 'D' for decrypt.")
                continue
            
            # User input for the message
            message = input("Enter your message: ")

            while True:
                # User input for the shift value with error handling
                shift = int(input("Enter shift value (0-25): "))
                if shift < 0:
                    print("Shift value should be a non-negative integer between 0 and 25. Please try again.")
                elif shift > 25:
                    print("Shift value should not exceed 25. Please try again.")
                elif shift == 0:
                    print("A shift value of 0 will result in no change to the message.")
                    proceed = input("Do you want to proceed with no change? (Y/N): ").strip().upper()
                    if proceed == 'Y':
                        break  # Accept shift of 0 and proceed
                    else:
                        continue  # Ask for shift value again
                else:
                    break  # Exit the loop if the shift is valid

            if action == 'E':
                # Encrypt the message
                encrypted_message = caesar_cipher(message, shift)
                print(f"Encrypted Message: {encrypted_message}")
            else:
                # Decrypt the message
                decrypted_message = caesar_cipher(message, -shift)
                print(f"Decrypted Message: {decrypted_message}")

            break  # Exit the loop after processing

        except ValueError:
            print("Invalid input. Please enter a valid integer for the shift value.")

if __name__ == "__main__":
    main()
