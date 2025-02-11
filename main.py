"""
This module provides the main interface for interacting with the habit tracker.
"""
import questionary
import plyer
from Habits import Habit
from analytics import Analytics
from reminder import Reminder
from database import Database

"""
Thhis main function runs the habit tracker
"""
def main():
    db = Database()
    db.connect()
    db.create_tables()

"""
Provides a main menu function where the user can make a selection
"""
    while True:
        user_selection = questionary.select(
            "What would you like to do?",
            choices=["Add Habit", "View Habits", "Set Reminder", "Exit"],
        ).ask()

"""
Adds a new habit
"""
        if user_selection == "Add Habit":
            name = questionary.text("Enter habit name:").ask()
            habit_type = questionary.text("Enter habit type:").ask()
            periodicity = questionary.text("Enter habit periodicity (daily/ weekly):").ask()
            start_date = questionary.text("Enter start date (YYYY-MM-DD):").ask()
            end_date = questionary.text("Enter end date (YYYY-MM-DD):").ask()
            description = questionary.text("Enter a description of the habit or any relevant notes:").ask()

            db.insert_habit(name, habit_type, periodicity, start_date=start_date, end_date=end_date, description)

"""
Lists habits
"""
        elif user_selection == "View Habits":
            habits = db.get_habits()
            if not habits:
                print("No habits found.")
                continue
            print("\nYour Habits:")
            for habit in habits:
                    print(f"- {habit.name}: {habit.habit_type}, {habit.periodicity}")
            habit_names =[habit.name for habit in habits]
            habit.names_append("Back to Main Menu")

            selected_habit = questionary.select(
                "Select a habit to view details:",
                choices=habit_names
            ).ask()

            if selected_habit == "Back to Main Menu":
                continue

            habit_action = [
                "View Analytics",
                "Remove Habit",
                "Check Completion",
                "Display Habit Details",
                "Back to Habits Menu"
                ]

            habit_action = questionary.select(
                f"What would you like to do with '{selected_habit}'?",
                choices=habit_actions
            ).ask()

"""
Provides analytics options
"""
            if habit_action == "View Analytics":
                analytics_menu = ["Get Total Habits", "Calculate Current Streak", "Calculate Longest Streak", "Calculate Completion Rate", "Reward Achievement", "Falling Off Target"]
                analytics_action = questionary.select(
                    f"Select an analytics option for '{selected_habit}':",
                    choices=analytics_menu
                ).ask()

                analytics = Analytics()

                if analytics_action == "Get Total Habits":
                    total_habits = analytics.get_total_habits()
                    print(f"Total habits tracked: {total_habits}")

                elif analytics_action == "Calculate Current Streak":
                    streak = analytics.calculate_current_streak(selected_habit)
                    print(f"Current streak for {selected_habit}: {streak} days")

                elif analytics_action == "Calculate Longest Streak":
                    longest_streak = analytics.calculate_longest_streak(selected_habit)
                    print(f"Longest streak for {selected_habit}: {longest_streak} days")

                elif analytics_action == "Calculate Completion Rate":
                    completion_rate = analytics.calculate_completion_rate(selected_habit)
                    print(f"Completion rate for {selected_habit}: {completion_rate}%")

                elif analytics_action == "Reward Achievement":
                    reward = analytics.reward_achievement(selected_habit)
                    print(f"Reward for {selected_habit}: {reward}")

                elif analytics_action == "Falling Off Target":
                    falling_off = analytics.falling_off_target(selected_habit)
                    print(f"Falling off target analysis for {selected_habit}: {falling_off}")

                elif analytics_action == "Back to Habit":
                    pass
            
            elif habit_action == "Remove Habit":
                db.remove_habit(select_habit)

            
            elif habit_action == "Check Completion":
                is_completed = db.check_completion(select_habit)
                print(f"Habit '{select_habit}' completion status: {'Completed' if is_completed else 'Not completed yet'}.")

            elif habit_action == "Display Habit Details":
                habit_details = db.get_habit_details(select_habit)
                print(f"Details for '{select_habit}':\n{display_habit_details}")

            elif habit_action == "Back to Habits Menu":
                continue
                

"""
Set a reminder for a particular habit
"""
        elif user_selection == "Set Reminder":
            habits = db.get_habits()
            if not habits :
                print("No habits found. Add habit first")
                continue
            
            habit_names = [habit.name for habit in habits]
            habit_names.append("Back to Main Menu")

            select_habit = questionary.select(
                "What habit do you want a reminder for?",
                choices=habit_names
            ).ask()

            if select_habit == "Back to Main Menu":
                continue
            
            reminder_time = questionary.text(
                f"Enter reminder time for {selected_habit}' (HH:MM format):"
            ).ask()

            message = (f"Time to complete your habit: {select_habit}!")

            reminder = Reminder(select_habit)
            reminder.schedule_reminder(reminder_time, message)

            print(f"Reminder set for '{select_habit}' at {reminder_time}!")
        
        elif user_selection == "Exit":
            db.close()
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()


            