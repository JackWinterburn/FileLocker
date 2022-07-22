from delete import delete
from create import create
from read import read

action = input("What would you like to do? (read, create or delete)")

if action == "read":
    read()
elif action == "create":
    create()
elif action == "delete":
    delete()
else:
    print("Looks like you typed in a non-existant command.")