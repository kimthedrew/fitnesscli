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
from helpers import (
    add_user, 
    add_workout_session, 
    view_workouts,
    delete_workout
)
import sys

def main_menu():
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
    main_menu()

