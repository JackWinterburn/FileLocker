from hash import Hash, GenKey
from cryptography.fernet import Fernet

def create():
    title = input("Please input the title of this new file: ")
    content = input("Please input the content of the new file: ")
    passwd = Hash(input("Please input the password you would like to use for this file: "))

    key = GenKey(passwd)
    f = Fernet(key)
    encrypted_content = f.encrypt(content.encode())

    print(encrypted_content)

create()
