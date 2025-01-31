"""
This module displays the Habit Class for enabling the user to log a habit
"""

from datetime import datetime


class Habit:

    valid_periodicity = ["Daily", "Weekly"]
    valid_habit_types = ["Health", "Productivity",
                         , "Social", "Other"]

    def __init__(self, name, habit_type, periodicity, start_date, end_date, completion_check, notes):
        self.name = name
        self.habit_type = habit_type
        self.periodicity = periodicity
        self.start_date = self.validate_date(start_date)
        self.end_date = self.validate_date(end_date)
        self.notes = notes if notes is not None else []
        self.completion_check = False

    def add_habit(self):
        print(f"You have added {self.name}. Let's go!")

    def remove_habit(self):
        print(f"You have removed {self.name}.")

    def edit_habit(self):
        print(f"You have made changes to {self.name}.")

    def update_notes(self, new_note):
        self.notes.append(new_note)

    def completion_check(self, completed: bool):
        self.completion_check = completed
        if self.completed:
            print(f"'{self.name}' has been marked as completed for today!")
        else:
            print(f"'{self.name}' has not been completed for today")

    def display_habit_details(self):
        print(f"Habit details:")
        print(f"Name: {self.name}")
        print(f"Type: {self.habit_type}")
        print(f"Periodicity: {self.periodicity}")
        print(f"Start Date: {self.start_date}")
        print(
            f"End Date: {self.end_date if self.end_date else 'Not specified'} ")
        print(
            f"Notes: {', '.join(self.notes) if self.notes else 'No notes added'}")

    def validate_date(self, date_str):
        try:
            return datetime.strptime(date_str, "%Y-%m-%d"). date()
        except ValueError:
            raise ValueError(
                f"Invalid date format: '{date_str}'. Expected format is YYYY-MM-DD.")

    def validate_periodicity(self, periodicity):
        if periodicity not in self.valid_periodicity:
            raise ValueError(
                f"Invalid periodicity: {periodicity}'. Choode from {self.valid_periodicity}.")
        return periodicity

    def validate_habit_type(self, habit_type):
        if habit_type not in self.valid_habit_types:
            raise ValueError(
                f"Invalid habit type: '{habit_type}'. Choose from {self.valid_habit_types}.")
        return habit_type
