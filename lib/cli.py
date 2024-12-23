# lib/cli.py

# from helpers import (
#     exit_program,
#     helper_1
# )


# def main():
#     while True:
#         menu()
#         choice = input("> ")
#         if choice == "0":
#             exit_program()
#         elif choice == "1":
#             helper_1()
#         else:
#             print("Invalid choice")


# def menu():
#     print("Please select an option:")
#     print("0. Exit the program")
#     print("1. Some useful function")


# if __name__ == "__main__":
#     main()

# cli.py

from lib.helpers import (
    display_welcome,
    add_user, 
    add_workout_session, 
    view_workouts,
    delete_workout
)

import sys
from lib.db.session import engine
from lib.models.model_1 import Base

Base.metadata.create_all(engine)

def main_menu():
    display_welcome()


    while True:
        print("\nFitness Tracker CLI")
        print("1. Add User")
        print("2. Add Workout Session")
        print("3. View Workouts")
        print("4. Delete Workout")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_user()
        elif choice == '2':
            add_workout_session()
        elif choice == '3':
            view_workouts()
        elif choice == '4':
            delete_workout()
        elif choice == '5':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid option. Please try again.")
        
if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

