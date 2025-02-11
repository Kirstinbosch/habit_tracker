"""
This module displays the Habit Class for enabling the user to log a habit
"""

from datetime import datetime

"""
Initializes a habit
"""
class Habit:

    valid_periodicity = ["Daily", "Weekly"]

    def __init__(self, habit_id: int, name: str, , periodicity: str, start_date: date, end_date: date, completion_check: bool, description: str):
        self.name = name
        self.periodicity = periodicity
        self.start_date = self.validate_date(start_date)
        self.end_date = self.validate_date(end_date)
        self.description = description if description is not None else []
        self.completion_check = False

"""
Adds new habit
"""
    def add_habit(self):
        print(f"You have added {self.name}. Let's go!")


"""
Removes a habit
"""
    def remove_habit(self):
        print(f"You have removed {self.name}.")


"""
Log signifying if a habit has been completed for the day/ week
"""
    def completion_check(self, completed: bool):
        self.is_completed = completed
        if self.is_completed:
            print(f"'{self.name}' has been marked as completed for today!")
        else:
            print(f"'{self.name}' has not been completed for today")

"""
Display all available habit details
"""
    def display_habit_details(self):
        print(f"Habit details:")
        print(f"Name: {self.name}")
        print(f"Periodicity: {self.periodicity}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date if self.end_date else 'Not specified'} ")
        print(f"Description: {', '.join(self.notes) if self.notes else 'No notes added'}")

"""
Ensures that the date is included in the correct format
"""
    def validate_date(self, date_str):
        try:
            return datetime.strptime(date_str, "%Y-%m-%d"). date()
        except ValueError:
            raise ValueError(
                f"Invalid date format: '{date_str}'. Expected format is YYYY-MM-DD.")

"""
Ensures that the periodicity is either daily or weekly
"""
    def validate_periodicity(self, periodicity):
        if periodicity not in self.valid_periodicity:
            raise ValueError(
                f"Invalid periodicity: {periodicity}'. Choode from {self.valid_periodicity}.")
        return periodicity

 
