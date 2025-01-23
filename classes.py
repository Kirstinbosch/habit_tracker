

class Habit:
    def __init__(self, name, habit_type, goal_hit_per_week, start_date, end_date, notes):
        self.name = name
        self.habit_type = habit_type
        self.goal_hit_per_week = goal_hit_per_week
        self.start_date = start_date
        self.end_date = None
        self.notes = []

    def add(self):
        print(f"You have added {__name__}. Let's go!")

    def remove(self):
        print(f"You have removed {__name__}. Loser.")

    def update_notes(self, new_note):
        self.notes.append(new_note)


class Analytics:
    def __init__(self, current_streak, longest_streak):
        self.current_streak = current_streak
        self.longest_streak = longest_streak

    def get_streak(self):
        return self.current_streak

    def longest_streak(self):
        return self.longest_streak

    def reset_streak(self):
        self.current_streak = 0




