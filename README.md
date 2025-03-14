# Gym Buddy - Personalized Training Planner

## Overview
Gym Buddy is a command-line application designed to help users create and manage personalized workout plans. With support for structured training plans, exercise tracking and progress monitoring, Gym Buddy is an essential tool for fitness enthusiasts and trainers.

## Features
- **Create, update, and delete training plans**
- **Add exercises to training plans**
- **List all training plans and exercises**
- **Find training plans and exercises by name or ID**
- **Display workout details in a beautifully formatted table using `rich`**
- **Enhanced terminal output styling with `colorama`**

## Technologies Used
- **Python** (CLI-based application)
- **Rich** (for beautiful terminal output, tables, and formatting)
- **Colorama** (for terminal color enhancements)
- **SQLite** (for persistent data storage)

## Installation
### Prerequisites
Ensure you have Python (>=3.8) installed and `pip` available.

### Clone the Repository
```sh
git clone https://github.com/yourusername/gym-buddy.git
cd gym-buddy
```

### Create a Virtual Environment
```sh
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# OR
.venv\Scripts\activate  # On Windows
```

### Install Dependencies
```sh
pipenv install
```

## Usage
### Running the Application
```sh
python3 cli.py
```

### Available Commands
- **Create a training plan**
  - Prompts for the name, goal, and duration of the training plan.
- **List all training plans**
  - Displays all training plans in a formatted table.
- **Find a training plan by name or ID**
  - Prompts for the name or ID and displays the corresponding training plan.
- **Add exercises to a training plan**
  - Prompts for the training plan ID and exercise details (name, muscle group, sets, reps).
- **List all exercises**
  - Displays all exercises in a formatted table.
- **Find an exercise by name or ID**
  - Prompts for the name or ID and displays the corresponding exercise.
- **Update a training plan or exercise**
  - Prompts for the ID and new details to update the training plan or exercise.
- **Delete a training plan or exercise**
  - Prompts for the ID and deletes the corresponding training plan or exercise.
- **List exercises in a training plan**
  - Prompts for the training plan ID and displays all exercises in that plan.

## Contributing

1. Fork the repository
2. Create a new branch (feature-xyz)
3. Commit your changes
4. Push to the branch and submit a Pull Request

## License

This project is licensed under the MIT License.