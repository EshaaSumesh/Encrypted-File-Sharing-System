from app.auth import register, login
from app.file_handler import secure_store, secure_retrieve
from crypto.rsa_utils import generate_keys

private_key, public_key = generate_keys()

print("\nEncrypted File Sharing System \n")

while True:
    print("1. Register")
    print("2. Login")
    print("3. Upload File")
    print("4. Download File")
    print("5. Exit")

    choice = input("\nSelect option: ")

    if choice == "1":
        u = input("Username: ")
        p = input("Password: ")
        register(u, p)
        print("User registered.\n")

    elif choice == "2":
        u = input("Username: ")
        p = input("Password: ")
        if login(u, p):
            print("Login successful.\n")
        else:
            print("Invalid credentials.\n")

    elif choice == "3":
        path = input("Enter file path: ")
        secure_store(path, public_key)
        print("File encrypted & stored securely.\n")

    elif choice == "4":
        name = input("Enter filename: ")
        secure_retrieve(name, private_key)
        print("File decrypted & restored.\n")

    elif choice == "5":
        break
