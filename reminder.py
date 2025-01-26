from datetime import datetime
from plyer import notification

class Reminder:
    def __init__(self, name: str, habit_id: int, reminder_time: str, message: str, frequency: str):
        self.name = name 
        self.habit_id = habit_id
        self.reminder_time = self.validate_datetime(reminder_time)
        self.message = message
        self.frequency = frequency
        self.is_active
    
    def validate_datetime(self, datetime_str: str):
        try: 
            return datetime. strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError(f"Invalid datetime format: '{datetime_str}'. Expected format is YYY-MM-DD HH:MM:SS.")
        
    def __str__(self):
        return(f"Reminder for {habit}: {self.message} at {self.reminder_time}."

    def send_reminder(self):
        notification.notify(title = (f"Time for '{self.name}'"),
        message = self.message,
        timeout = 10)
    
    def schedule_reminder(self, reminder_time: str, message: str):
        self.reminder_time = self.validate_datetime(reminder_time)
        self.message = message
        print(f"Reminder scheduled for habit '{self.name}' at {self.reminder_time}.")
    
    def trigger_reminder(self):
        if self.is_active:  # Ensure the reminder is not cancelled
            current_time = datetime.datetime.now()
            if current_time >= self.reminder_time:
                self.send_reminder()
                print(f"Reminder for Habit '{self.name}' triggered at {current_time}.")
            else:
                print(f"Reminder for Habit '{self.name}' is scheduled for {self.reminder_time}.")
        else:
            print(f"Reminder for Habit '{self.name}' is cancelled and will not trigger.")
        
    def update_reminder(self, reminder_time: str = None, message: str = None, frequency: str = None):
        if reminder_time:
            self.reminder_time = self.validate_datetime(reminder_time)
        if message:
            self.message = message
        if frequency:
            self.frequency = frequency
        print(f"Reminder for habit '{self.name}' updated.")

    def cancel_reminder(self):
        self.is_active = False
        print(f"Reminder for habit '{self.name}' has been cancelled.")
    
     def retrieve_reminder_details(self):
        return {
            'habit_id': self.habit_id,
            'name': self.name,
            'reminder_time': self.reminder_time,
            'message': self.message,
            'frequency': self.frequency
        }

        




