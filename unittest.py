"""
This module contains the test cases for the Habit Tracking application.
"""

import unittest
from habits import Habit
from unittest.mock import patch
from reminder import Reminder


class TestHabit(unittest.TestCase):
    def setUp(self):
        self.habit = Habit("Yoga", "Health", "weekly", "2025-01-01", "vinyasa")

     def test_habit_creation(self):
        """Test if habit is created correctly"""
        self.assertEqual(self.habit.name, "Yoga")
        self.assertEqual(self.habit.habit_type, "Health")
        self.assertEqual(self.habit.periodicity, "weekly")
        self.assertEqual(self.habit.start_date, "2025-01-01")
        self.assertEqual(self.habit.notes, "vinyasa")

class TestReminder(unittest.TestCase):
    def setUp(self):
        self.reminder = Reminder(name="Yoga", reminder_time="08:00", message="Time to work out!", frequency="daily")


    def test_reminder_creation(self):
        self.assertEqual(self.reminder.name, "Yoga")
        self.assertEqual(self.reminder.message, "Time to work out!")

    @patch("plyer.notification.notify")  
    def test_send_notification(self, mock_notify):
        self.reminder.send_notification()
        mock_notify.assert_called_once_with(title="Time for 'Exercise'", message="Time to work out!", timeout=10)
    
    def setUp(self):
        self.habit1 = Habit(
            name="Exercise",
            periodicity="daily",
            start_date="2025-01-01",
            end_date="2025-31-01","
            description="Run like you mean it",
        )
        self.habit1.completion_check = [True, True, True, False, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, False, True, True, True, False, False, False]

        self.habit2 = Habit(
            name="Reading",
            periodicity="weekly",
            start_date="2025-01-01",
            description="Read Books",
        )
        self.habit2.completion_check = [True, True, True, False]

        self.analytics1 = Analytics(self.habit1)
        self.analytics2 = Analytics(self.habit2)

        def test_calculate_current_streak_daily(self):
        """Test the calculate_current_streak method for a daily habit."""
        today = datetime.today()

        days_since_start = (today - self.habit1.start_date).days
        expected_streak = days_since_start

        streak = self.analytics1.calculate_current_streak()

        self.assertIn(f"The streak for {self.habit1.name} is {expected_streak} days", streak)

    def test_calculate_current_streak_weekly(self):
        """Test the calculate_current_streak method for a weekly habit."""
    
        today = datetime.today()

        days_since_start = (today - self.habit2.start_date).days
        expected_streak = days_since_start // 7 

  
        streak = self.analytics2.calculate_current_streak()


        self.assertIn(f"The streak for {self.habit2.name} is {expected_streak} days", streak)




if __name__ == "__main__":
    unittest.main()


