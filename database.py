import sqlite3


class Database:
    def __init__(self, db_name="habits.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        print(f"Connected to database: {self.db_name}")

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS habits (
                habit_id INTEGER PRIMARY KEY,
                name TEXT,
                periodicity TEXT,
                time_spent TEXT
                start_date TEXT,
                end_date TEXT,
                description TEXT,
                completion_check TEXT
            )
        """)
        self.connection.commit()
        print("Table created.")

    def insert_habit(self, name: str, habit_id: int, periodicity: str, time_spent: str = None, start_date: str, end_date: str = None, description: str = None):
        try:
            self.cursor.execute("""
                INSERT INTO habits (name, habit_type, periodicity, start_date, end_date, description, completion_check)
                VALUES (?,?,?,?,?,?,?)
            """, (name, habit_type, periodicity,
                                start_date, time_spent, end_date, description, completion_check))
            self.connection.commit()
            print(
                f"Habit '{name}' has been successfully added to the database")
        except sqlite3.Error as e:
            print(f"An error occured while inserting the habit: {e}")

    def get_habits(self) -> List[Habits]:
        try:
            self.cursor.execute("SELECT * FROM habits")
            rows = self.cursor.fetchall()
            habits = [
                Habit(
                    habit_id=row[0],
                    name=row[1],
                    habit_type=row[2],
                    periodicity=row[3],
                    time_spent=row[4],
                    start_date=row[5],
                    end_date=row[6],
                    description=row[7]
                ) for row in rows
            ]
            return habits
        except sqlite3.Error as e:
            print(f"An error occured while retrieving habits: {e}")
            return []


    def delete_habit(self, habit_id: int):
        try:
            self.cursor.execute("""
                DELETE FROM habits
                WHERE habit_id = ?
            """, (habit_id,))
            self.connection.commit()
            print(f"Habit with ID {habit_id} has been deleted")
        except sqlite3.Error as e:
            print(f"An error occured while deleting the habit: {e}")

    def close(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
