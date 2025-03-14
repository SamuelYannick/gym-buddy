from training_plan import TrainingPlan
from exercise import Exercise
from colorama import Fore, Style
from rich.console import Console
from rich.table import Table

console = Console()

def exit_program():
    console.print("Keep those muscles popping for me! Be consistent.", style="bold red")
    exit()

def list_training_plans():
    plans = TrainingPlan.get_all()
    table = Table(title="Training Plans")
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Goal", style="yellow")
    for plan in plans:
        table.add_row(str(plan.id), plan.name, plan.goal)
    console.print(table)

def find_training_plan_by_name():
    name = input("Enter the training plan's name: ")
    plan = TrainingPlan.find_by_name(name)
    console.print(plan if plan else f"[red]Training plan {name} not found[/red]")

def find_training_plan_by_id():
    id_ = input("Enter the training plan's id: ")
    plan = TrainingPlan.find_by_id(id_)
    console.print(plan if plan else f"[red]Training plan {id_} not found[/red]")

def create_training_plan():
    name = input("Enter the training plan's name: ")
    goal = input("Enter the training goal: ")
    duration = int(input("Enter the training duration (weeks): "))  # Ensure duration is provided
    try:
        plan = TrainingPlan.create(name, goal, duration)
        console.print(f"[green]Success: {plan}[/green]")
    except Exception as e:
        console.print(f"[red]Error creating training plan: {e}[/red]")

def update_training_plan():
    id_ = input("Enter the training plan's id: ")
    if plan := TrainingPlan.find_by_id(id_):
        try:
            name = input("Enter the training plan's new name: ")
            goal = input("Enter the training goal: ")
            duration = int(input("Enter the training duration (weeks): "))  # Ensure duration is provided
            plan.name = name
            plan.goal = goal
            plan.duration = duration
            plan.update()
            console.print(f"[green]Success: {plan}[/green]")
        except Exception as exc:
            console.print(f"[red]Error updating training plan: {exc}[/red]")
    else:
        console.print(f"[red]Training plan {id_} not found[/red]")

def delete_training_plan():
    id_ = input("Enter the training plan's id: ")
    if plan := TrainingPlan.find_by_id(id_):
        plan.delete()
        console.print(f"[red]Training plan {id_} deleted[/red]")
    else:
        console.print(f"[red]Training plan {id_} not found[/red]")

def list_exercises():
    exercises = Exercise.get_all()
    table = Table(title="Exercises")
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Muscle Group", style="yellow")
    for exercise in exercises:
        table.add_row(str(exercise.id), exercise.name, exercise.muscle_group)
    console.print(table)

def find_exercise_by_name():
    name = input("Enter the exercise's name: ")
    exercise = Exercise.find_by_name(name)
    console.print(exercise if exercise else f"[red]Exercise {name} not found[/red]")

def find_exercise_by_id():
    id_ = input("Enter the exercise's id: ")
    exercise = Exercise.find_by_id(id_)
    console.print(exercise if exercise else f"[red]Exercise {id_} not found[/red]")

def create_exercise():
    name = input("Enter the exercise's name: ")
    muscle_group = input("Enter the muscle group: ")
    sets = int(input("Enter the number of sets: "))  # Ensure sets is provided
    reps = int(input("Enter the number of reps: "))  # Ensure reps is provided
    training_plan_id = int(input("Enter the training plan ID: "))  # Ensure training_plan_id is provided
    try:
        exercise = Exercise.create(name, muscle_group, sets, reps, training_plan_id)
        console.print(f"[green]Success: {exercise}[/green]")
    except Exception as e:
        console.print(f"[red]Error creating exercise: {e}[/red]")

def update_exercise():
    id_ = input("Enter the exercise's id: ")
    if exercise := Exercise.find_by_id(id_):
        try:
            name = input("Enter the exercise's new name: ")
            muscle_group = input("Enter the muscle group: ")
            sets = int(input("Enter the number of sets: "))  # Ensure sets is provided
            reps = int(input("Enter the number of reps: "))  # Ensure reps is provided
            exercise.name = name
            exercise.muscle_group = muscle_group
            exercise.sets = sets
            exercise.reps = reps
            exercise.update()
            console.print(f"[green]Success: {exercise}[/green]")
        except Exception as exc:
            console.print(f"[red]Error updating exercise: {exc}[/red]")
    else:
        console.print(f"[red]Exercise {id_} not found[/red]")

def delete_exercise():
    id_ = input("Enter the exercise's id: ")
    if exercise := Exercise.find_by_id(id_):
        exercise.delete()
        console.print(f"[red]Exercise {id_} deleted[/red]")
    else:
        console.print(f"[red]Exercise {id_} not found[/red]")

def add_exercise_to_plan():
    plan_id = input("Enter the training plan's id: ")
    plan = TrainingPlan.find_by_id(plan_id)

    if not plan:
        console.print(f"[red]Training plan {plan_id} not found[/red]")
        return

    exercise_id = input("Enter the exercise's id: ")
    exercise = Exercise.find_by_id(exercise_id)

    if not exercise:
        console.print(f"[red]Exercise {exercise_id} not found[/red]")
        return

    # Check if exercise is already in the plan
    existing_exercises = plan.get_exercises()
    if any(ex.id == exercise.id for ex in existing_exercises):
        console.print(f"[yellow]Exercise '{exercise.name}' is already in the training plan '{plan.name}'![/yellow]")
        return

    # Add the exercise to the plan
    try:
        plan.add_exercise(exercise)
        console.print(f"[green]Successfully added '{exercise.name}' to '{plan.name}'![/green]")
    except Exception as e:
        console.print(f"[red]Error adding exercise: {e}[/red]")

def list_plan_exercises():
    plan_id = input("Enter the training plan's id: ")
    if plan := TrainingPlan.find_by_id(plan_id):
        exercises = plan.get_exercises()
        table = Table(title=f"Exercises in Training Plan {plan.name}")
        table.add_column("ID", style="cyan")
        table.add_column("Name", style="green")
        table.add_column("Muscle Group", style="yellow")
        for exercise in exercises:
            table.add_row(str(exercise.id), exercise.name, exercise.muscle_group)
        console.print(table)
    else:
        console.print(f"[red]Training plan {plan_id} not found[/red]")