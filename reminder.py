from datetime import datetime
from plyer import notification

class Reminder:
    def __init__(self, name: str, habit_id: int, reminder_time: str, message: str):
        self.name = name 
        self.habit_id = habit_id
        self.reminder_time = self.validate_datetime(reminder_time)
        self.message = message
        self.is_active = True
    
    def validate_datetime(self, datetime_str: str):
        try: 
            return datetime. strptime(datetime_str, "%H:%M")
        except ValueError:
            raise ValueError(f"Invalid datetime format: '{datetime_str}'. Expected format is HH:MM")
        
    def __str__(self):
        return(f"Reminder for {self.name}: {self.message} at {self.reminder_time}.")

    def send_notification(self):
        notification.notify(title = (f"Time for '{self.name}'"),
        message = self.message,
        timeout = 10)
    
    def schedule_reminder(self, reminder_time: str, message: str):
        self.reminder_time = self.validate_datetime(reminder_time)
        self.message = message
        print(f"Reminder scheduled for habit '{self.name}' at {self.reminder_time}.")
        
    def update_reminder(self, reminder_time: str = None, message: str = None, frequency: str = None):
        if reminder_time:
            self.reminder_time = self.validate_datetime(reminder_time)
        if message:
            self.message = message
        if frequency:
            self.frequency = frequency
        print(f"Reminder for habit '{self.name}' updated.")

    def cancel_reminder(self):
        self.is_active = True
        print(f"Reminder for habit '{self.name}' has been cancelled.")
    
     def retrieve_reminder_details(self):
        return {
        'habit_id': self.habit_id,
        'name': self.name,
        'reminder_time': self.reminder_time,
        'message': self.message,
        'frequency': self.frequency
        }

        




