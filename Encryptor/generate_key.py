from cryptography.fernet import Fernet

# Generate and save the key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

generate_key()
print("Encryption key generated and saved as 'secret.key'.")
