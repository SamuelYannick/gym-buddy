from __init__ import CURSOR, CONN

class TrainingPlan:
    all = {}  # Dictionary to store all TrainingPlan instances
    
    def __init__(self, id, name, goal, duration):
        self.id = id
        self.name = name
        self.goal = goal
        self.duration = duration
        TrainingPlan.all[self.id] = self  # Ensure the instance is added to the all dictionary
    
    def __repr__(self):
        return f"<TrainingPlan {self.id}: {self.name}, Goal: {self.goal}, Duration: {self.duration} weeks>"
    
    @classmethod
    def create_table(cls):
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS training_plans (
                id INTEGER PRIMARY KEY,
                name TEXT,
                goal TEXT,
                duration INTEGER
            )
        ''')
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        CURSOR.execute("DROP TABLE IF EXISTS training_plans")
        CONN.commit()
    
    def save(self):
        CURSOR.execute("INSERT INTO training_plans (name, goal, duration) VALUES (?, ?, ?)",
                       (self.name, self.goal, self.duration))
        CONN.commit()
        self.id = CURSOR.lastrowid  # Get the last inserted row id
        TrainingPlan.all[self.id] = self
    
    @classmethod
    def get_all(cls):
        rows = CURSOR.execute("SELECT * FROM training_plans").fetchall()
        return [cls(id=row[0], name=row[1], goal=row[2], duration=row[3]) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        row = CURSOR.execute("SELECT * FROM training_plans WHERE name = ?", (name,)).fetchone()
        return cls(id=row[0], name=row[1], goal=row[2], duration=row[3]) if row else None

    @classmethod
    def find_by_id(cls, id_):
        row = CURSOR.execute("SELECT * FROM training_plans WHERE id = ?", (id_,)).fetchone()
        return cls(id=row[0], name=row[1], goal=row[2], duration=row[3]) if row else None

    @classmethod
    def create(cls, name, goal, duration):
        plan = cls(id=None, name=name, goal=goal, duration=duration)
        plan.save()
        return plan

    def update(self):
        CURSOR.execute("UPDATE training_plans SET name = ?, goal = ?, duration = ? WHERE id = ?",
                       (self.name, self.goal, self.duration, self.id))
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM training_plans WHERE id = ?", (self.id,))
        CONN.commit()
        if self.id in TrainingPlan.all:
            del TrainingPlan.all[self.id]  # Ensure the instance is removed from the all dictionary

    def add_exercise(self, exercise):
        exercise.training_plan_id = self.id  # Set the training plan ID for the exercise
        exercise.save()

    def get_exercises(self):
        from exercise import Exercise
        rows = CURSOR.execute("SELECT * FROM exercises WHERE training_plan_id = ?", (self.id,)).fetchall()
        return [Exercise(*row) for row in rows]
