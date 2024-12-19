# lib/helpers.py

# def helper_1():
#     print("Performing useful function#1.")


# def exit_program():
#     print("Goodbye!")
#     exit()
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.db import session
from lib.db.models import User

def add_user():
    try:
        name = input("Enter name: ").strip()
        email = input("Enter email: ").strip()

        if not name or not email:
            print("Name and email cannot be empty. Please try again.")
            return
    

        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        print(f"User {name} added successfully!")
    except Exception as e:
        print(f"An error occured while adding the user: {e}")


