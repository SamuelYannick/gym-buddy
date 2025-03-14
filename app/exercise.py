from __init__ import CURSOR, CONN

class Exercise:
    all = {}  # Dictionary to store all Exercise instances
    
    def __init__(self, id, name, muscle_group, sets, reps, training_plan_id):
        self.id = id
        self.name = name
        self.muscle_group = muscle_group
        self.sets = sets
        self.reps = reps
        self.training_plan_id = training_plan_id
        Exercise.all[self.id] = self  # Ensure the instance is added to the all dictionary
    
    def __repr__(self):
        return f"<Exercise {self.id}: {self.name}, Muscle Group: {self.muscle_group}, Sets: {self.sets}, Reps: {self.reps}>"
    
    @classmethod
    def create_table(cls):
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS exercises (
                id INTEGER PRIMARY KEY,
                name TEXT,
                muscle_group TEXT,
                sets INTEGER,
                reps INTEGER,
                training_plan_id INTEGER,
                FOREIGN KEY (training_plan_id) REFERENCES training_plans(id)
            )
        ''')
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        CURSOR.execute("DROP TABLE IF EXISTS exercises")
        CONN.commit()
    
    def save(self):
        CURSOR.execute("INSERT INTO exercises (name, muscle_group, sets, reps, training_plan_id) VALUES (?, ?, ?, ?, ?)",
                       (self.name, self.muscle_group, self.sets, self.reps, self.training_plan_id))
        CONN.commit()
        self.id = CURSOR.lastrowid  # Get the last inserted row id
        Exercise.all[self.id] = self
    
    @classmethod
    def get_all(cls):
        rows = CURSOR.execute("SELECT * FROM exercises").fetchall()
        return [cls(id=row[0], name=row[1], muscle_group=row[2], sets=row[3], reps=row[4], training_plan_id=row[5]) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        row = CURSOR.execute("SELECT * FROM exercises WHERE name = ?", (name,)).fetchone()
        return cls(id=row[0], name=row[1], muscle_group=row[2], sets=row[3], reps=row[4], training_plan_id=row[5]) if row else None

    @classmethod
    def find_by_id(cls, id_):
        row = CURSOR.execute("SELECT * FROM exercises WHERE id = ?", (id_,)).fetchone()
        return cls(id=row[0], name=row[1], muscle_group=row[2], sets=row[3], reps=row[4], training_plan_id=row[5]) if row else None

    @classmethod
    def create(cls, name, muscle_group, sets, reps, training_plan_id):
        exercise = cls(id=None, name=name, muscle_group=muscle_group, sets=sets, reps=reps, training_plan_id=training_plan_id)
        exercise.save()
        return exercise

    def update(self):
        CURSOR.execute("UPDATE exercises SET name = ?, muscle_group = ?, sets = ?, reps = ?, training_plan_id = ? WHERE id = ?",
                       (self.name, self.muscle_group, self.sets, self.reps, self.training_plan_id, self.id))
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM exercises WHERE id = ?", (self.id,))
        CONN.commit()
        if self.id in Exercise.all:
            del Exercise.all[self.id]  # Ensure the instance is removed from the all dictionary
