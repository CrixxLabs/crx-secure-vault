import os
from cryptography.fernet import Fernet
from .key_manager import derive_key

def encrypt_file(file_path: str, password: str):
    with open(file_path, 'rb') as f:
        data = f.read()

    salt = os.urandom(16)
    key = derive_key(password, salt)
    fernet = Fernet(key)

    encrypted = fernet.encrypt(data)

    with open(file_path + ".crx", 'wb') as f:
        f.write(salt + encrypted)

    print("✅ File encrypted.")

def decrypt_file(file_path: str, password: str):
    with open(file_path, 'rb') as f:
        content = f.read()

    salt = content[:16]
    encrypted_data = content[16:]

    key = derive_key(password, salt)
    fernet = Fernet(key)

    decrypted = fernet.decrypt(encrypted_data)

    original_name = file_path.replace(".crx", "")

    with open(original_name, 'wb') as f:
        f.write(decrypted)

    print(" File decrypted.")