"""
This module displays the Reminder Class for sending notifications to the user
"""


from datetime import datetime
from plyer import notification

"""
Initializes the reminder
"""
class Reminder:
    def __init__(self, name: str, habit_id: int, reminder_time: str, message: str):
        self.name = name 
        self.habit_id = habit_id
        self.reminder_time = self.validate_datetime(reminder_time)
        self.message = message
        self.is_active = True
    
"""
Ensures that the date is included in the correct format
"""
    def validate_datetime(self, datetime_str: str):
        try: 
            return datetime.strptime(datetime_str, "%H:%M")
        except ValueError:
            raise ValueError(f"Invalid datetime format: '{datetime_str}'. Expected format is HH:MM")
        
    def __str__(self):
        return(f"Reminder for {self.name}: {self.message} at {self.reminder_time}.")

"""
Delivers a notification to the user which is displayed on the screen for 10 seconds
"""
    def send_notification(self):
        notification.notify(title = (f"Time for '{self.name}'"),
        message = self.message,
        timeout = 10)

"""
Sets a reminder with time and message included
""" 
    def schedule_reminder(self, reminder_time: str, message: str):
        self.reminder_time = self.validate_datetime(reminder_time)
        self.message = message
        print(f"Reminder scheduled for habit '{self.name}' at {self.reminder_time}.")

"""
Cancels the reminder, but does not delete the data from the system
"""
    def cancel_reminder(self):
        self.is_active = False
        print(f"Reminder for habit '{self.name}' has been cancelled.")

 """
Check up on reminder details
"""   
     def retrieve_reminder_details(self):
        return {
        'habit_id': self.habit_id,
        'name': self.name,
        'reminder_time': self.reminder_time,
        'message': self.message,
        }

        




