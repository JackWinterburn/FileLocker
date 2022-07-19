import os.path
from hash import Hash, GenKey, bcrypt
from cryptography.fernet import Fernet

def create():
    title   = input("Please input the title of this new file: ")
    content = input("Please input the content of the new file: ")
    passwd  = Hash(input("Please input the password you would like to use for this file: "))

    key = GenKey(passwd)
    f   = Fernet(key)
    encrypted_content = f.encrypt(content.encode())

    if os.path.exists(f"./lockers/{title}.txt"):
        raise Exception("File already exists, unable to overwrite locked file")
    else:         
        with open(f"./lockers/{title}.txt", "w") as f:
            f.write(encrypted_content.decode())
        with open(f"passes.txt", "a") as f:
            f.write(f"\n{title}: {passwd.decode()}")

create()
