import bcrypt
import os
from cryptography.fernet import Fernet
from read import findPass

def delete():
    title = input("What is the name of the file that you want to delete?: ")
    if not os.path.exists(f"./lockers/{title}.txt"):
        raise Exception("File does not exist, unable to delete non-existant file")

    password = input("Please enter the password for this file: ")
    ogPass = findPass(title)

    if bcrypt.checkpw(password.encode(), ogPass.encode()):
        os.remove(f"./lockers/{title}.txt")
        with open("passes.txt", "r") as f:
            lines = f.readlines()
        with open("passes.txt") as f:
            for line in enumerate(lines):
                fn = line[1]
                fn = fn[:fn.find(":")]
                if fn == title:
                    with open("passes.txt", "w") as f:
                        for n, l in enumerate(lines):
                            if not n == line[0]:
                                f.write(l)
                
               

    else:
        print("Error: Passwords don't match")
