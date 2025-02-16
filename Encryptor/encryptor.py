from cryptography.fernet import Fernet
import os

# Generate or load encryption key
KEY_FILE = "secret.key"

def generate_key():
    """Generate a new encryption key and save it to a file."""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def load_key():
    """Load the encryption key from a file."""
    if not os.path.exists(KEY_FILE):
        generate_key()
    return open(KEY_FILE, "rb").read()

key = load_key()
cipher = Fernet(key)

def encrypt_email(email):
    """Encrypt an email address."""
    encrypted_email = cipher.encrypt(email.encode())
    return encrypted_email.decode()

def decrypt_email(encrypted_email):
    """Decrypt an encrypted email address."""
    decrypted_email = cipher.decrypt(encrypted_email.encode())
    return decrypted_email.decode()
