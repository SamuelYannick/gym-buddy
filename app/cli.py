from helpers import (
    exit_program,
    list_training_plans,
    find_training_plan_by_name,
    find_training_plan_by_id,
    create_training_plan,
    update_training_plan,
    delete_training_plan,
    list_exercises,
    find_exercise_by_name,
    find_exercise_by_id,
    create_exercise,
    update_exercise,
    delete_exercise,
    list_plan_exercises,
    add_exercise_to_plan
)

from colorama import Fore, Style, init
from rich.console import Console
from rich.table import Table

init(autoreset=True)  # Initialize colorama for automatic reset of styles
console = Console()

def main():
    while True:
        menu()
        choice = input(Fore.CYAN + "> " + Style.RESET_ALL)  # Display prompt in cyan color
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_training_plans()
        elif choice == "2":
            find_training_plan_by_name()
        elif choice == "3":
            find_training_plan_by_id()
        elif choice == "4":
            create_training_plan()
        elif choice == "5":
            update_training_plan()
        elif choice == "6":
            delete_training_plan()
        elif choice == "7":
            list_exercises()
        elif choice == "8":
            find_exercise_by_name()
        elif choice == "9":
            find_exercise_by_id()
        elif choice == "10":
            create_exercise()
        elif choice == "11":
            update_exercise()
        elif choice == "12":
            delete_exercise()
        elif choice == "13":
            list_plan_exercises()
        elif choice == "14":
            add_exercise_to_plan()
        else:
            console.print("[bold red]Invalid choice. Please try again.[/bold red]")

def menu():
    table = Table(title="Gym Buddy - Training Planner")
    table.add_column("Option", style="cyan", justify="right")
    table.add_column("Action", style="magenta")
    
    options = [
        ("0", "Exit the program"),
        ("1", "List all training plans"),
        ("2", "Find training plan by name"),
        ("3", "Find training plan by ID"),
        ("4", "Create training plan"),
        ("5", "Update training plan"),
        ("6", "Delete training plan"),
        ("7", "List all exercises"),
        ("8", "Find exercise by name"),
        ("9", "Find exercise by ID"),
        ("10", "Create exercise"),
        ("11", "Update exercise"),
        ("12", "Delete exercise"),
        ("13", "List exercises in a training plan"),
        ("14", "Add exercise to training plan")
    ]
    
    for option, action in options:
        table.add_row(option, action)
    
    console.print(table)

if __name__ == "__main__":
    main()
