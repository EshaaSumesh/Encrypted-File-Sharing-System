from crypto.cryptoaes_utils import generate_aes_key, encrypt_file, decrypt_file
from crypto.cryptorsa_utils import encrypt_key, decrypt_key
import os


def secure_store(file_path, public_key):
    with open(file_path, 'rb') as f:
        data = f.read()

    aes_key = generate_aes_key()
    encrypted_data = encrypt_file(data, aes_key)
    encrypted_key = encrypt_key(aes_key, public_key)

    filename = os.path.basename(file_path)
    with open(f"storage/{filename}.enc", 'wb') as f:
        f.write(encrypted_data)

    with open(f"storage/{filename}.key", 'wb') as f:
        f.write(encrypted_key)


def secure_retrieve(filename, private_key):
    with open(f"storage/{filename}.enc", 'rb') as f:
        encrypted_data = f.read()

    with open(f"storage/{filename}.key", 'rb') as f:
        encrypted_key = f.read()

    aes_key = decrypt_key(encrypted_key, private_key)
    data = decrypt_file(encrypted_data, aes_key)

    with open(f"storage/{filename}", 'wb') as f:
        f.write(data)
