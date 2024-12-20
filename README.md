# WorkoutPal

WorkoutPal is a command-line interface (CLI) application designed to help users manage their fitness journey. Users can register, log workout sessions, view their progress, and delete outdated sessions, all from the comfort of their terminal.

## Features

- **Add Users:** Register new users by providing a name and email.
- **Log Workouts:** Record workout sessions with details such as type, duration, and associated user.
- **View Workouts:** List all recorded workout sessions.
- **Delete Workouts:** Remove outdated or incorrect workout sessions.

## Technologies Used

- **Python 3.8+**
- **SQLAlchemy:** For ORM-based database interactions.
- **SQLite:** Lightweight database for data storage.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.8 or later
- pip (Python package installer)

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/workoutpal.git
   cd workoutpal
   ```

2. Set up a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database:

   ```bash
   python -m lib.db.init
   ```

## Usage

Run the application:

```bash
python -m lib.cli
```

### Main Menu

- **1. Add User:** Enter a user's name and email to register them.
- **2. Add Workout Session:** Record a workout session for a specific user.
- **3. View Workouts:** Display all recorded workout sessions.
- **4. Delete Workout:** Remove a workout session by its ID.
- **5. Exit:** Exit the application.

## Project Structure

```
workoutpal/
├── lib/
│   ├── cli.py          # Main CLI application
│   ├── helpers.py      # Helper functions for CLI operations
│   ├── db/
│   │   ├── session.py  # Database session and engine setup
│   │   ├── init.py     # Database initialization script
│   │   └── models.py   # SQLAlchemy models (User, WorkoutSession)
│   └── __init__.py
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .gitignore          # Git ignored files
```

## Example

1. **Add User:**
   ```
   Enter choice: 1
   Enter name: John Doe
   Enter email: john.doe@example.com
   User added successfully!
   ```

2. **Log Workout Session:**
   ```
   Enter choice: 2
   Enter workout type: Running
   Enter workout duration (in minutes): 30
   Enter user ID: 1
   Workout session added successfully!
   ```

3. **View Workouts:**
   ```
   Enter choice: 3
   ID: 1, Type: Running, Duration: 30, User ID: 1
   ```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests with improvements.

## License

This project is licensed under the MIT License.
