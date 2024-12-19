# lib/helpers.py

# def helper_1():
#     print("Performing useful function#1.")


# def exit_program():
#     print("Goodbye!")
#     exit()
# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# print("Importing session...")
# from lib.db.session import session
# print("session imported successfully")
# from lib.models.model_1 import User

# def add_user():
#     try:
#         name = input("Enter name: ").strip()
#         email = input("Enter email: ").strip()

#         if not name or not email:
#             print("Name and email cannot be empty. Please try again.")
#             return
    

#         user = User(name=name, email=email)
#         session.add(user)
#         session.commit()
#         print(f"User {name} added successfully!")
#     except Exception as e:
#         print(f"An error occured while adding the user: {e}")
        
# def display_welcome():
#     print("Welcome to the fitnesss tracker CLI!")
# def add_workout_session():
#     print("This feature is under development.")

from lib.db.session import session
from lib.models.model_1 import User, WorkoutSession

def display_welcome():
    print("Welcome to the Fitness Tracker CLI!")

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
        print(f"An error occurred while adding the user: {e}")

def add_workout_session():
    try:
        workout_type = input("Enter workout type: ").strip()
        duration = input("Enter workout duration (in minutes): ").strip()
        user_id = input("Enter user ID: ").strip()

        if not workout_type or not duration or not user_id:
            print("Workout details cannot be empty. Please try again.")
            return

        workout_session = WorkoutSession(
            workout_type=workout_type,
            duration=int(duration),
            user_id=int(user_id)
        )
        session.add(workout_session)
        session.commit()
        print("Workout session added successfully!")
    except Exception as e:
        print(f"An error occurred while adding the workout session: {e}")

def view_workouts():
    try:
        workouts = session.query(WorkoutSession).all()
        for workout in workouts:
            print(f"Workout: {workout.workout_type}, Duration: {workout.duration} minutes, Date: {workout.date}")
    except Exception as e:
        print(f"An error occurred while viewing the workouts: {e}")

def delete_workout():
    try:
        workout_id = input("Enter workout session ID to delete: ").strip()
        if not workout_id:
            print("Workout ID cannot be empty.")
            return

        workout = session.query(WorkoutSession).get(int(workout_id))
        if workout:
            session.delete(workout)
            session.commit()
            print(f"Workout session with ID {workout_id} deleted.")
        else:
            print("Workout session not found.")
    except Exception as e:
        print(f"An error occurred while deleting the workout session: {e}")
