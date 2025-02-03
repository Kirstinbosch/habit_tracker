from datetime import datetime

class Analytics:
    def __init__(self, habit_id: int, total_habits: int, longest_streak: int, current_streak: int, completion_rate: float)
        self.habit_id = habit_id
        self.total_habits = total_habits
        self.longest_streak = longest_streak
        self.current_streak = current_streak
        self.completion_rate = completion_rate    
    

    def get_total_habits(self):
        return(f"Total number of habits. {len(self.total_habits)}")

    def calculate_current_streak(self):
        streak = (datetime.today() - self.habit.start_date).days
        return(f"The streak for {self.habit.name} is {streak} days")

    def calculate_longest_streak(self):
        longest_streak = 0
        longest_habit = None

        for habit in self.habits:
            streak = habit.calculate_current_streak()
            print(f"{habit.name} streak: {streak} days")

        if streak > longest_streak:
            longest_streak = streak
            longest_habit = habit

        return(f"The longest streak is {longest_streak} days for the habit: {longest_habit.name}")

    def get_total_days(self):
        return (datetime.today() - self.habit.start_date).days + 1

    def calculate_completion_rate(self):
        total_days = self.get_total_days()
        if self.habit.periodicity == "daily"
         potential_completions = total_days
        else self.habit.periodicity == "weekly"
          potential_completions = (total_days // 7) + (1 if total_days % 7 != 0 else 0)
    
        actual_completions = len(self.habit.completions)

        completion_rate = (actual_completions / potential_completions) * 100
            return completion_rate

    
# def calculate_habits_by_periodicity(self)

    def reward_achievement(self):
        if self.habit.end_date < datetime.today():
            if all(self.habit.completion_check):
                return(f"Congratulations! You have successfully completed your habit: {self.habit.name}.")


    def falling_off_target(self):
        missed_streak = 0
            for i, completed in enumerate(self.habit.completion_check):
                if not completed:
                    missed_streak += 1
                else:
                    missed_streak = 0
                if missed_streak == 3:
                    return(f"You're falling off target for your habit: {self.habit.name}.")

