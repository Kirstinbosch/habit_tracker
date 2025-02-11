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



if __name__ == "__main__":
    unittest.main()


