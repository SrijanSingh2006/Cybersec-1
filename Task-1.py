import string

def caesar_cipher(text, shift, mode="encrypt"):
    result = ""

    if mode == "decrypt":
        shift = -shift  # Reverse the shift for decryption

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        elif char.isdigit():  # Shift numbers (optional)
            result += str((int(char) + shift) % 10)
        else:
            result += char  # Keep spaces and special characters unchanged

    return result

def main():
    while True:
        print("\n--- Caesar Cipher Tool ---")
        mode = input("Enter mode (encrypt/decrypt): ").strip().lower()

        if mode not in ["encrypt", "decrypt"]:
            print("Invalid mode! Please enter 'encrypt' or 'decrypt'.")
            continue

        text = input("Enter the message: ").strip()
        try:
            shift = int(input("Enter shift value (integer): "))
        except ValueError:
            print("Invalid shift! Please enter a valid integer.")
            continue

        output = caesar_cipher(text, shift, mode)
        print(f"Result: {output}")

        again = input("\nDo you want to run again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
