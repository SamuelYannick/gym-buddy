from training_plan import TrainingPlan
from exercise import Exercise
import random

# Create tables before seeding data, avoid error "no such table"
TrainingPlan.create_table()
Exercise.create_table()

def seed_training_plans():
    """Seeds the database with realistic training plans."""
    training_plans = [
        {"name": "Beginner Strength", "goal": "Build foundational strength", "duration": 8},
        {"name": "Fat Loss", "goal": "Lose body fat and improve cardiovascular health", "duration": 12},
        {"name": "Muscle Gain", "goal": "Increase muscle mass", "duration": 10},
        {"name": "Endurance Training", "goal": "Improve stamina and endurance", "duration": 6},
        {"name": "Flexibility Routine", "goal": "Enhance flexibility and mobility", "duration": 4}
    ]
    
    for plan in training_plans:
        created_plan = TrainingPlan.create(name=plan["name"], goal=plan["goal"], duration=plan["duration"])
        print(f"Seeded Training Plan: {created_plan}")

def seed_exercises():
    """Seeds the database with realistic exercises."""
    exercises = [
        {"name": "Bench Press", "muscle_group": "Chest", "sets": 4, "reps": 10},
        {"name": "Squat", "muscle_group": "Legs", "sets": 4, "reps": 12},
        {"name": "Deadlift", "muscle_group": "Back", "sets": 3, "reps": 8},
        {"name": "Bicep Curl", "muscle_group": "Arms", "sets": 3, "reps": 15},
        {"name": "Shoulder Press", "muscle_group": "Shoulders", "sets": 4, "reps": 10},
        {"name": "Plank", "muscle_group": "Core", "sets": 3, "reps": 60},  # 60 seconds hold
        {"name": "Lunges", "muscle_group": "Legs", "sets": 3, "reps": 12},
        {"name": "Pull-Up", "muscle_group": "Back", "sets": 3, "reps": 10},
        {"name": "Tricep Dip", "muscle_group": "Arms", "sets": 3, "reps": 12},
        {"name": "Leg Raise", "muscle_group": "Core", "sets": 3, "reps": 15}
    ]
    
    training_plans = TrainingPlan.get_all()
    if not training_plans:
        print("No training plans found. Please seed training plans first.")
        return

    for exercise in exercises:
        training_plan = random.choice(training_plans)  # Randomly assign an exercise to a training plan
        created_exercise = Exercise.create(
            name=exercise["name"],
            muscle_group=exercise["muscle_group"],
            sets=exercise["sets"],
            reps=exercise["reps"],
            training_plan_id=training_plan.id
        )
        print(f"Seeded Exercise: {created_exercise}")

if __name__ == "__main__":
    print("Seeding database...")
    seed_training_plans()
    seed_exercises()
    print("Seeding complete!")
