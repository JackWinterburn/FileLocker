import bcrypt
import os.path
from hash import GenKey
from cryptography.fernet import Fernet

def read():
    title = input("What is the name of the file that you want to read?: ")
    if not os.path.exists(f"./lockers/{title}.txt"):
        raise Exception("File does not exist, unable to unlock non-existant file")

    password = input("Please enter the password for this file: ")
    ogPass = findPass(title)

    if bcrypt.checkpw(password.encode(), ogPass.encode()):
        with open(f"./lockers/{title}.txt", "r") as f:
            txt = f.read()
            content = txt[:txt.find("-||-")].encode()
            key = txt[txt.find("-||-")+4:].encode()

            fnet = Fernet(key)
            print(fnet.decrypt(content).decode())
    else:
        print("Error: Passwords don't match")
    





def findPass(filename):
    '''
    Takes in the filename of an encrypted text file
    reads passes.txt file to find the password associated with the given filename
    returns the hashed password of the filename provided
    '''
    with open("passes.txt", "r") as f:
        content    = f.read()
        start      = content.find(f"{filename}:")
        end        = content.find("\n", start)
        hashedPswd = content[start+len(filename)+2:end]
        return hashedPswd

read()