from cryptography.fernet import Fernet
import os

# Generate and save key
def create_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)
    print("\n✅ Key created: key.key")

# Load the saved key
def get_key():
    return open("key.key", "rb").read()

# Main Program Loop
print("=== Simple Encrypt / Decrypt Tool ===")

while True:
    print("\n1. Create Key")
    print("2. Encrypt")
    print("3. Decrypt")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        create_key()

    elif choice == "2":
        try:
            key = get_key()
            f = Fernet(key)
            text = input("Enter text to encrypt: ")
            encrypted = f.encrypt(text.encode())
            print("🔒 Encrypted:", encrypted.decode()) # decoded for cleaner display
        except FileNotFoundError:
            print("❌ Error: Key not found. Please run Option 1 first.")

    elif choice == "3":
        try:
            key = get_key()
            f = Fernet(key)
            encrypted_msg = input("Enter encrypted text: ")
            # We need to encode the input string back to bytes for decryption
            decrypted = f.decrypt(encrypted_msg.encode()).decode()
            print("🔓 Decrypted:", decrypted)
        except Exception as e:
            print("❌ Error: Could not decrypt. Wrong key or invalid text.")

    elif choice == "4":
        print("Exiting...")
        break
    
    else:
        print("Invalid option")