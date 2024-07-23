from cryptography.fernet import Fernet
import json

def get_login_info() -> dict:
    # Read the decryption key file, and get key
    with open('login_info/filekey.key', 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    # Read the decrypted file
    with open("login_info/login_info.json", "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    # decode byte type and load json into dictionary
    return json.loads(decrypted.decode('utf-8'))