# lib/helpers.py

# def helper_1():
#     print("Performing useful function#1.")


# def exit_program():
#     print("Goodbye!")
#     exit()

from lib.db import session
from lib.db.models import User

def add_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    print(f"User {name} added successfully!")

