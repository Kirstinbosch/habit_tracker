
"""
This module analyzes habits stored in the database.
"""

from datetime import datetime

"""
Initializes the analytics class
"""
class Analytics:
    def __init__(self, habit_id: int, total_habits: int, longest_streak: int, current_streak: int, completion_rate: float)
        self.habit_id = habit_id
        self.total_habits = total_habits
        self.periodicity = periodicity 
        self.longest_streak = longest_streak
        self.current_streak = current_streak
        self.completion_rate = completion_rate    
    
"""
Counts the total number of logged habits
"""
    def get_total_habits(self):
        return(f"Total number of habits. {len(self.total_habits)}")

"""
Calculates the current streak of a particular habit
"""
    def calculate_current_streak(self):
        days_since_start = (datetime.today() - self.habit.start_date).days
        if self.habit.periodicity == "daily":
            streak = days_since_start
        elif self.habit.periodicity == "weekly":
            streak = days_since_start // 7
        else:
            streak = 0
        
        return(f"The streak for {self.habit.name} is {streak} days")

"""
Calculates which habit has the longest streak
"""
    def calculate_longest_streak(self):
        longest_streak = 0
        longest_habit = None

        for habit in self.habits:
            streak = habit.calculate_current_streak()
            if habit.periodicity == "weekly":
                streak = streak // 7

            print(f"{habit.name} streak: {streak} {'weeks' if habit.periodicity == 'weekly' else 'days'}")

        if streak > longest_streak:
            longest_streak = streak
            longest_habit = habit

        return f"The longest streak is {longest_streak} {'weeks' if longest_habit.periodicity == 'weekly' else 'days'} for the habit: {longest_habit.name}"

"""
Calculates the total amount of days a habit has been performed for
"""
    def get_total_days(self):
        return (datetime.today() - self.habit.start_date).days + 1

"""
Calculates the completion rate of selected habit
"""
    def calculate_completion_rate(self):
        total_days = self.get_total_days()
        if self.habit.periodicity == "daily"
            potential_completions = total_days
        elif self.habit.periodicity == "weekly"
            potential_completions = (total_days // 7) + (1 if total_days % 7 != 0 else 0)
    
        actual_completions = len(self.habit.completions)

        if potential_completions == 0:
            compeltion_rate = 0
        else:
            completion_rate = (actual_completions / potential_completions) * 100
            
        return completion_rate

"""
Rewards an achievement if the habit has an end date, and this date has passed and if the completion rate is 100 percent, or all the completion checks have been completed True
"""
    def reward_achievement(self):
        if self.habit.end_date < datetime.today():
            if completion_rate == 100 or all(self.habit.completion_check):
                return(f"Congratulations! You have successfully completed your habit: {self.habit.name}.")

"""
Displays a message if the habit has been missed three times in a row
"""
    def falling_off_target(self):
        missed_streak = 0
            for i, completed in enumerate(self.habit.completion_check):
                if not completed:
                    missed_streak += 1
                else:
                    missed_streak = 0
                if missed_streak == 3:
                    return(f"You're falling off target for your habit: {self.habit.name}.")

