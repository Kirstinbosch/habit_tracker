**MY HABIT TRACKER IN PYTHON**

This Python habit tracker application is designed to help users create, manage, and analyze
habits on a periodic basis (daily and weekly). The application tracks user engagement with
habits and provides basic analytics, such as identifying the longest streak of a habit and
highlighting habits that receive the least attention. This application is written in Python 
code and it uses SQLite as the backend database to store and manage the data. Users can 
interact with the application via the command-line interface (CLI).

__________________________________________________________________________________________________________

**INSTALLATION INSTRUCTIONS**

Dependencies
Python 3.7+

1. Clone the repository

        git clone [https://github.com/yourusername/your-repo.git](https://github.com/Kirstinbosch/habit_tracker.git)

        cd habit_tracker

2. Create and activate a virtual environment

        python -m venv venv

        venv\Scripts\activate (Windows) 
        source venv/bin/activate (Linux)

3. Install dependencies

        pip install -r requirements.txt

4. (When finished) Deactivate virtual enviornment

        deactivate

__________________________________________________________________________________________________________

**Usage Instructions**

1. Run the python script

        python main.py

From uploading the main.py file, the user will be asked what they would like to do in the program and they will be presented with a main menu with the following options: "Enter habit", "View Habits", "Set reminder", "Exit". The user can intuitively navigate the application and perform different functions such as creating habits, viewing current habits, logging entries of habits, and running a number of statistics on the habits to understand progress.

__________________________________________________________________________________________________________

**Using .gitignore**

In order to maintin cleanliness of the repository, include a .gitignore file. This file will avoid committing files that are machine-specific or auto-generated.

The .git ignore file includes:

        venv/             # Virtual environment folder 
        .vscode/          # VS Code settings, extensions, and configurations
        __pycache__/      # Python cache files  
        *.pyc             # Compiled Python files  
        .DS_Store         # macOS system file  
        .env              # Environment variables (if applicable)  

Implement .gitignore:

1. Remove any accidently added ignored files

        git rm -r --cached venv/

2. Committ the change

        git commit -m "Updated .gitignore to exclude unnecessary files"

3. Push the changes

        git push origin main









